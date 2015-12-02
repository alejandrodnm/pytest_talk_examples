def sum(x, y):
    return x + y


def div(x, y):
    return x / y


def raises_custom(name):
    raise CustomError('Raise for {}'.format(name))


class CustomError(Exception):
    pass
