import logging as _logging


def create_logger(app):
    """

    :param app:
    :return:
    """
    logger = _logging.getLogger('hakka.app')
    handler = _logging.StreamHandler()

    if app.debug and logger.level == _logging.NOTSET:
        handler.setLevel(_logging.DEBUG)
        logger.setLevel(_logging.DEBUG)
        logger.addHandler(handler)
    return logger
