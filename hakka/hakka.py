from os import environ as env
import redis
import json
from logging import StreamHandler, getLogger
import asyncio

logger = getLogger(__name__)
handler = StreamHandler()


# 別スレッドで、状態を返す

redis_vtypes = {
    'str': str,
    'int': int,
    'float': float,
    'bool': bool,
    'json': json.loads,
}


def cast_redis_value(val, _vtype):
    """

    :param val:
    :param _vtype:
    :return:
    :rtype: str or int or float or bool or dict
    """
    # FIXME: jsonでparseできない場合に落ちる
    _cast = redis_vtypes.get(_vtype)
    return _cast(val)


class Hakka(object):
    _config = {}
    _keys = []
    _running = False
    _beat = 0.01
    _loop = None

    def __init__(self):
        self.conn = None
        self.debug = False

    def listen(self, host=None, port=None, db=None, debug=False):
        self._loop = asyncio.get_event_loop()
        self.debug = debug
        self.conn = redis.Redis(host=host, port=port, db=db)
        self.watch_task_queue()
        self._loop.run_forever()

    def watch(self, key=None, redis_dtype='LIST', redis_vtype='str'):
        def _watch(callback):
            self._config.update({
                key: {
                    'callback': callback,
                    'redis:dtype': redis_dtype,
                    'redis:vtype': redis_vtype,
                }
            })
            self._keys.append(key)
            return callback

        return _watch

    def _run_task(self):
        for key in self._keys:
            params = self._config.get(key)
            data = None
            redis_dtype = params.get('redis:dtype')

            pipe = self.conn.pipeline()
            pipe.watch(key)

            if redis_dtype == 'list':
                data = pipe.lpop(key)
                # TODO lpoprpushして、エラー時の対応をする

            if redis_dtype == 'str':
                data = pipe.get(key)
                # TODO エラー時の対応
                self.conn.delete(key)

            # Break: TODO: timeout
            if data is None:
                continue

            # Cast:
            redis_vtype = params.get('redis:vtype')
            callback = params.get('callback')

            callback_args = cast_redis_value(data, redis_vtype)
            if redis_vtype == 'json':
                callback(**callback_args)
            else:
                callback(callback_args)
        self._loop.call_later(self._beat, self._run_task)

    def watch_task_queue(self):
        logger.debug("watch keys: {}".format(self._keys))
        self._loop.call_soon(self._run_task)


if __name__ == '__main__':
    from logging import DEBUG

    handler.setLevel(DEBUG)
    logger.setLevel(DEBUG)
    logger.addHandler(handler)

    app = Hakka()


    @app.watch('hello:msg', redis_dtype='list', redis_vtype='json')
    def hello_msg(name=None, msg=None, **kwargs):
        print("Hello {name}!, {msg}".format(name=name, msg=msg))


    @app.watch('test:good', redis_dtype='list', redis_vtype='json')
    def hello(name=None, good=None, **kwargs):
        logger.debug("=" * 30)
        logger.debug(name)
        logger.debug(good)
        logger.debug(kwargs)


    app.listen(host=env.get('REDIS_HOST'), port=env.get('REDIS_PORT'), db=env.get('REDIS_DB'), debug=True)
