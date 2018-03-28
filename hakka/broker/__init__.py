import abc


class BaseBroker:

    @abc.abstractmethod
    def ping(self):
        pass

    def liveness_probe(self):
        pass


from .redis import RedisBroker


def make_broker(host=None, port=None, db=None, _broker_type='redis'):
    """
    Redis, mongoDBの両方に対応する
    :return:
    """
    return RedisBroker(host=host, port=port, db=db)
