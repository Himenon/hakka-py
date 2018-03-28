from os import environ as env
import asyncio
from .broker import make_broker
from .exceptions import (
    HakkaConnectionError,
    HakkaTimeoutError,
)
from .logging import create_logger


# 別スレッドで、状態を返す
class Hakka(object):
    _config = {}
    _loop = None
    _retry_counter = 0

    def __init__(self):
        self.conn = None
        self.debug = False
        self.max_retry_count = 60
        self.retry_connection_interval = 5
        self.beat_interval = 0.01
        self.timeout = 30
        self.watch_keys = []

    def listen(self, host=None, port=None, db=None, debug=False):
        self._loop = asyncio.get_event_loop()
        self.debug = debug
        self.conn = make_broker(host=host, port=port, db=db)
        self.watch_tasks()
        self._loop.run_forever()

    def watch(self, key=None, *args, **kwargs):
        if key is None:
            raise ValueError("'key' argument should be other than None.")

        def _watch(callback):
            self._config.update({
                key: {
                    'callback': callback,
                }
            })
            self.watch_keys.append(key)
            return callback

        return _watch

    def get_func(self, key):
        return self._config.get(key).get('callback')

    def run_task(self):
        for key in self.watch_keys:
            if not self.conn.llen(key) > 0:
                continue
            callback = self.get_func(key)
            arguments = self.conn.get_value(key)
            callback(**arguments)

    # TODO cached_property
    @property
    def logger(self):
        return create_logger(self)

    def watch_tasks(self):
        try:
            self.run_task()  # タスクの実行
            self._loop.call_soon(self.beat_interval, self.watch_tasks)  # タスクの再実行
        except HakkaConnectionError:
            # 再実行
            self._retry_counter += 1
            self.logger.error("Retry Redis connection .... {}".format(self._retry_counter))
            self._loop.call_later(self.retry_connection_interval, self.watch_tasks)
        except HakkaTimeoutError:
            self.logger.error("Timeout Error")
            pass
        self._retry_counter = 0


# if __name__ == '__main__':
#     app = Hakka()
#
#
#     @app.watch('hello:msg')
#     def hello_msg(name=None, msg=None, **kwargs):
#         print("Hello {name}!, {msg}".format(name=name, msg=msg))
#
#
#     @app.watch('test:good')
#     def hello(name=None, good=None, **kwargs):
#         logger.debug("=" * 30)
#         logger.debug(name)
#         logger.debug(good)
#         logger.debug(kwargs)
#
#
#     app.listen(host=env.get('REDIS_HOST'), port=env.get('REDIS_PORT'), db=env.get('REDIS_DB'), debug=True)
