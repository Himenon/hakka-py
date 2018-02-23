"""
redisと接続するための場所
"""
import redis


def get_redis(host, port, db):
    return redis.Redis(host=host, port=port, db=db)
