import pytest
from mock import patch


# from redis.client import Redis


# @patch('redis.Redis', mock_redis_client)
# def test_make_client(client):
#     conn = make_client(host='test-redis')
#     assert issubclass(type(conn), Redis)


def test_hello_redis(client):
    client.lpush("hello", "world")
    actual = client.lpop("hello").decode("utf-8")
    assert "world" == actual


def test_get_value(client):
    input_key = "app-name"
    input_val = {
        "name": "hakka",
        "lang": "python",
        "year": 2017,
    }
    client.set_value(input_key, input_val)
    actual_vals = client.get_value(input_key)
    assert input_val["name"] == actual_vals["name"]
    assert input_val["lang"] == actual_vals["lang"]
    assert input_val["year"] == actual_vals["year"]
