from hakka import HakkaRedisClient, Hakka
from os import environ

if __name__ == '__main__':
    client = HakkaRedisClient(
        host=environ.get('REDIS_HOST', 'localhost'),
        port=environ.get('REDIS_PORT', 6379)
    )
    app = Hakka(client, debug=True)


    @app.watch('hello:msg')
    def hello_msg(name=None, msg=None, **kwargs):
        app.logger.debug("Hello {name}!, {msg}".format(name=name, msg=msg))
        app.logger.debug(kwargs)


    app.listen()
