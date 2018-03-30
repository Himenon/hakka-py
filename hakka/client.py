from redis import Redis
from hakka.types import HakkaType, cast_broker_value
from .utils import bytes_to_str
import json
from redis.exceptions import ConnectionError


class BaseHakkaClient(object):
    pass


class HakkaRedisMixin(BaseHakkaClient):
    _connected = False
    logger = None

    def check_connection(self):
        try:
            self.ping()
            if self._connected is False:
                self.logger.info("==== Success Connected Redis Client! ====")
            self._connected = True
        except ConnectionError:
            self._connected = False
        return self._connected

    def set_value(self, key, value):
        if not isinstance(value, dict):
            value = {
                "{}:raw_value".format(key): value
            }
        self.lpush(key, json.dumps(value))

    def get_value(self, key):
        pipe = self.pipeline()
        pipe.watch(key)
        raw_value = bytes_to_str(pipe.lpop(key))
        if raw_value:
            return cast_broker_value(raw_value, HakkaType.JSON)
        return raw_value


class HakkaRedisClient(HakkaRedisMixin, Redis):
    pass


def make_client(*args, **kwargs):
    return HakkaRedisClient(*args, **kwargs)
