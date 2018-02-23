from os import environ as env
from .conn import get_redis
from .queue import Queue


# 別スレッドで、状態を返す

class Toss(object):
    _callback = {}
    __keys = []
    _data_stores = {}
    _running = False

    def __init__(self):
        self.observer = None
        self.queue = None
        self.server = None

    @property
    def subscribed(self):
        return True

    def listen(self, host=None, port=None, db=None):
        self.server = get_redis(host=host, port=port, db=db)
        self.queue = Queue(self.server)
        self._run_pubspub()

    def _run_pubspub(self):
        self._running = True
        pubsub = self.server.pubsub()
        pubsub.subscribe(['channel'])
        recv_msg = True
        for item in pubsub.listen():
            print(item)
            if not recv_msg:
                break
            if item['data'] == b'__EOM__':
                pubsub.unsubscribe()
                recv_msg = False
        self.close()
        self._running = False

    def _connect(self):
        pass

    def register(self, kind, name, **kwargs):
        if kind == 'store':
            self._register_store(name, **kwargs)

    def _register_store(self, name, **kwargs):
        _type = kwargs.pop('type')
        self._data_stores.update({
            name: get_redis(**kwargs)
        })

    def pump(self, key, func):
        pass

    def stock(self, store_name, data=None):
        pass

    def send(self):
        pass

    def close(self):
        pass


if __name__ == '__main__':
    app = Toss()
    app.listen(host=env.get('REDIS_HOST'), port=env.get('REDIS_PORT'), db=env.get('REDIS_DB'))
