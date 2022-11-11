def add_name(cls):
    class _Inner:
        def __init__(self, *args, **kwargs):
            self._obj = cls(*args, **kwargs)
            self._name = ''

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, name):
            self._name = name

        def __getattr__(self, attr):
            return getattr(self._obj, attr)

    return _Inner


@add_name
class MyClass:
    def __init__(self):
        ...

    def tt(self):
        ...





