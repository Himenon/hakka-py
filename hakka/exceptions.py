class HakkaError(Exception):
    pass


class HakkaConnectionError(HakkaError):
    pass


class HakkaTimeoutError(HakkaError):
    pass
