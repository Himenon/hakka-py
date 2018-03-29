from hakka import HakkaRedisClient, Hakka

if __name__ == '__main__':
    client = HakkaRedisClient()
    app = Hakka(client, debug=True)

    @app.watch('hello:msg')
    def hello_msg(name=None, msg=None, **kwargs):
        app.logger.debug("Hello {name}!, {msg}".format(name=name, msg=msg))
        app.logger.debug(kwargs)

    app.listen()
