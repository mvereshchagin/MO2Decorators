from functools import wraps
import time


def timeit(f):
    """
    decorator to calc time of execution for any function
    :param f: function
    :return: decorator
    """
    @wraps(f)
    def inner(*args, **kwargs):
        start = time.perf_counter()
        f(*args, **kwargs)
        end = time.perf_counter()
        print(f'{f.__name__} {args}, {kwargs} time = {end - start}')
    return inner


def repeat(n: int):
    """
    decorator to repeat function call
    :param n: amount of calls
    :return: return decorator
    """
    def _repeat(f):
        @wraps(f)
        def inner(*args, **kwargs):
            for _ in range(n):
                f(*args, **kwargs)
        return inner
    return _repeat


def repeat_timeit(n: int):
    """
    decorator to calc execution time for n calls of function
    :param n: number of calls
    :return: decorator
    """
    def _repeat(f):
        @wraps(f)
        def inner(*args, **kwargs):
            start = time.perf_counter()
            for _ in range(n):
                f(*args, **kwargs)
            end = time.perf_counter()
            print(f'{n} calls {f.__name__} {args}, {kwargs} time = {end - start}')
        return inner
    return _repeat


def repeat_timeit2(f=None, *, n: int = 1):
    """
    decorator to calc execution time for n calls of function.
    Can be called with or without param n
    :param n: number of calls
    :return: decorator
    """
    def _repeat(f):
        @wraps(f)
        def inner(*args, **kwargs):
            start = time.perf_counter()
            for _ in range(n):
                f(*args, **kwargs)
            end = time.perf_counter()
            print(f'{n} calls {f.__name__} {args}, {kwargs} time = {end - start}')
        return inner
    if f is None:
        return _repeat
    else:
        return _repeat(f)