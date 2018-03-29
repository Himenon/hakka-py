from hakka import HakkaRedisClient

if __name__ == '__main__':
    client = HakkaRedisClient()

    message = {
        "name": "hakka",
        "reading": "books"
    }
    for i in range(10):
        message.update({
            "msg": "Hello World x {}!".format(i),
        })
        client.set_value('hello:msg', message)
