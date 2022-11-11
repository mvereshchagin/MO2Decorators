import time

from repeat_decorator import timeit, repeat_timeit, repeat_timeit2, repeat
from repeater import Repeater
from deco_class import MyClass
from timeit_deco_class import timeit_for_all_methods


def main() -> None:

    f = timeit(calc)
    f(2, 3)

    timeit(calc)(2, 3)

    calc2(3, 4)

    print(calc2.__doc__)

    print(calc.__doc__)

    print_hello()

    print(print_hello.__doc__)

    print('----------------------------------')
    repeat(10)(print_hello2)()

    test_loop(10)

    # test_loop2(10)

    test_loop2(10)

    test_loop3(100)

    test_loop4(100)

    test_deco_class()

    test_timeit_deco_class()


# region test functions
def test_deco_class():
    cls = MyClass()
    cls.name = 'Vasya'
    cls.tt()
    print(cls.name)


@timeit_for_all_methods
class Calcer:

    def calc3(self):
        time.sleep(3)

    def calc4(self):
        time.sleep(4)


def test_timeit_deco_class():
    calcer = Calcer()
    calcer.calc3()
    calcer.calc4()


def calc(a: int, b: int):
    """
    Calculates sum of two numbers
    :param a: number 1
    :param b: number 2
    :return: The sum
    """
    time.sleep(2)
    return a + b


@timeit
def calc2(a: int, b: int):
    """
    Calculates sum of two numbers
    :param a: number 1
    :param b: number 2
    :return: The sum
    """
    time.sleep(2)
    return a + b


@repeat(10)
def print_hello() -> None:
    """
    Prints hello
    :return: None
    """
    print('Hello')


def print_hello2():
    print('Hello')


@repeat_timeit(1000000)
def test_loop(count: int):
    lst = [i for i in range(count)]


@repeat_timeit2
def test_loop2(count: int):
    lst = [i for i in range(count)]


@Repeater(100)
def test_loop3(count: int) -> None:
    for i in range(count):
        i += 1


@Repeater()
def test_loop4(count: int) -> None:
    for i in range(count):
        i += 1











# endregion


if __name__ == '__main__':
    main()

