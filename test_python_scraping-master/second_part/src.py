
def random_gen():
    pass


def decorator_to_str(func):
    # todo exercise 2
    return func


@decorator_to_str
def add(a, b):
    return a + b


@decorator_to_str
def get_info(d):
    return d['info']


def ignore_exception(exception):
    # todo exercise 3
    return lambda x: x


@ignore_exception(ZeroDivisionError)
def div(a, b):
    return a / b


@ignore_exception(TypeError)
def raise_something(exception):
    raise exception


# exercise 4
class CacheDecorator:
    """Saves the results of a function according to its parameters"""
    def __init__(self):
        self.cache = {}

    def __call__(self, func):
        def _wrap(*a, **kw):
            if a[0] not in self.cache:
                self.cache[a[0]] = func(*a, **kw)
            return self.cache[a[0]]

        return _wrap


class MetaInherList(type):
    # todo exercise 5
    pass


class Ex:
    x = 4


class ForceToList(Ex, metaclass=MetaInherList):
    pass

