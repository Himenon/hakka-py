from .broker import make_broker


class HakkaClient:

    def __init__(self, host=None, port=None, db=None, debug=False):
        self.conn = make_broker(host=host, port=port, db=db)

    def register(self, key, value):
        if not isinstance(value, dict):
            value = {
                "{}:raw_value".format(key): value
            }
        self.conn.lpush(key, value)
