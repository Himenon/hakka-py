import pytest
import sys
from mockredis import mock_redis_client, mock_strict_redis_client
from mock import patch
from hakka import make_broker
from redis.client import Redis

sys.path.append('/src')


@patch('redis.Redis', mock_redis_client)
def test_hello_redis():
    conn = mock_redis_client()
    conn.lpush("hello", "world")
    actual = conn.lpop("hello").decode("utf-8")
    assert "world" == actual


@patch('redis.Redis', mock_redis_client)
def test_make_broker():
    """
    Redisのインスタンスを作成しているかどうか
    :return:
    """
    conn = make_broker(host='test-redis')
    assert issubclass(type(conn), Redis)

