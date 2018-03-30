from hakka import HakkaRedisClient
from os import environ

if __name__ == '__main__':
    client = HakkaRedisClient(
        host=environ.get('REDIS_HOST', 'localhost'),
        port=environ.get('REDIS_PORT', 6379)
    )

    message = {
        "name": "hakka",
        "reading": "books"
    }
    for i in range(10):
        message.update({
            "msg": "Hello World x {}!".format(i),
        })
        client.set_value('hello:msg', message)
