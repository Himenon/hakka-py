import asyncio
# from .exceptions import (
#     HakkaConnectionError,
#     HakkaTimeoutError,
# )
from redis.exceptions import ConnectionError as HakkaConnectionError
from redis.exceptions import TimeoutError as HakkaTimeoutError
from .logging import create_logger
from .helpers import locked_cached_property


# 別スレッドで、状態を返す
class Hakka(object):
    _config = {}
    _loop = None
    _retry_counter = 0
    testing = False
    connected = False

    def __init__(self, client, debug=False):
        self.debug = debug
        self.client = client
        self.client.logger = self.logger
        self.max_retry_count = 60
        self.retry_connection_interval = 5
        self.beat_interval = 0.01
        self.timeout = 30
        self._watch_keys = []

    def listen(self):
        self.logger.info("/* ---- Welcome to Hakka Application --- */")
        self._loop = asyncio.get_event_loop()
        self.watch_tasks()
        self._loop.run_forever()
        # self._loop.close()

    @property
    def watch_keys(self):
        if len(self._watch_keys) > 0:
            return self._watch_keys
        self._watch_keys = [k for k in self._config]
        return self.watch_keys

    def watch(self, key=None, *args, **kwargs):
        if key is None:
            raise ValueError("'key' argument should be other than None.")

        def _watch(callback):
            self._config.update({
                key: {
                    'callback': callback,
                }
            })
            return callback

        return _watch

    def get_func(self, key):
        return self._config.get(key).get('callback')

    def run_task(self):
        for key in self.watch_keys:
            if not self.client.llen(key) > 0:
                continue
            callback = self.get_func(key)
            arguments = self.client.get_value(key)
            callback(**arguments)

    @locked_cached_property
    def logger(self):
        return create_logger(self)

    def watch_tasks(self):
        try:
            self.client.check_connection()
            self.run_task()  # タスクの実行
            self._loop.call_later(self.beat_interval, self.watch_tasks)  # タスクの再実行
            self._retry_counter = 0
        except HakkaConnectionError:
            # 再実行
            self._retry_counter += 1
            self.logger.error("Retry Redis connection {} times.".format(self._retry_counter))
            # if self.max_retry_count == self._retry_counter:
            # self._loop.stop()
            # self.logger.error("/* ---- Shutdown Hakka Application ---- */")
            # else:
            self._loop.call_later(self.retry_connection_interval, self.watch_tasks)
        except HakkaTimeoutError:
            self.logger.error("Timeout Error")
        except Exception as e:
            self.logger.error("--- 予期せぬエラーが発生しました ---")
            self.logger.error(e)
