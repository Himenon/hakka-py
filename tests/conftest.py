import pytest
from hakka import Hakka
from hakka.client import HakkaRedisMixin
# from mockredis import mock_redis_client
from mockredis.client import MockRedis


class HakkaRedisClient(HakkaRedisMixin, MockRedis):
    pass


@pytest.fixture
def client():
    return HakkaRedisClient()


@pytest.fixture
def app(client):
    return Hakka(client=client)
