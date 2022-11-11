from repeat_decorator import timeit


def timeit_for_all_methods(cls):
    class _Inner:
        def __init__(self, *args, **kwargs):
            self._obj = cls(*args, **kwargs)

        def __getattribute__(self, item):
            try:
                x = super().__getattribute__(item)
            except AttributeError:
                pass
            else:
                return x

            attr = self._obj.__getattribute__(item)
            if isinstance(attr, type(self.__init__)):
                return timeit(attr)
            else:
                return attr

    return _Inner

