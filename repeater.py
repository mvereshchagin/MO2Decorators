import time
from functools import wraps


class Repeater:
    """
    Class-decorator to calc execution time of n calls of a function
    """
    def __init__(self, n: int = 1):
        self._n = n

    def __call__(self, f):
        @wraps(f)
        def inner(*args, **kwargs):
            start = time.perf_counter()
            for _ in range(self._n):
                f(*args, **kwargs)
            end = time.perf_counter()
            print(f'{self._n} calls {f.__name__} {args}, {kwargs} time = {(end - start):.4f}')

        return inner
