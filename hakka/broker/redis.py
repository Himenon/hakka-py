from . import BaseBroker
from redis import Redis
from hakka.types import HAKKA_VALUE_TYPES, cast_broker_value


class RedisBroker(Redis, BaseBroker):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_value(self, key):
        pipe = self.pipeline()
        pipe.watch(key)
        raw_value = pipe.lpop(key)
        return cast_broker_value(raw_value, HAKKA_VALUE_TYPES.JSON)
