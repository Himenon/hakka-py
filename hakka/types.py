from enum import Enum
import json


class HakkaType(Enum):
    BOOL = 1
    FLOAT = 2
    INTEGER = 3
    JSON = 4
    LIST = 5
    STRING = 6


HAKKA_VALUE_TYPES = {
    HakkaType.STRING: str,
    HakkaType.INTEGER: int,
    HakkaType.FLOAT: float,
    HakkaType.BOOL: bool,
    HakkaType.JSON: json.loads,
}


def cast_broker_value(raw_val, convert_type):
    # FIXME: jsonの場合にキャストできないことがある
    _cast = HAKKA_VALUE_TYPES.get(convert_type)
    return _cast(raw_val)
