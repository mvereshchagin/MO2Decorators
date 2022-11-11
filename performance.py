from repeat_decorator import repeat_timeit


def main():
    str_test()


def str_test():
    n = int(1e+6)
    str1, str2, str3 = 'val1', 'val2', 'val3'
    args = str1, str2, str3

    repeat = repeat_timeit(n)

    repeat(str_test_f)(*args)
    repeat(str_test_format_no_number)(*args)
    repeat(str_test_format_with_number)(*args)
    repeat(str_test_concat)(*args)
    repeat(str_test_join)(*args)

    n = 100
    repeat = repeat_timeit(n)

    count = int(1e+5)
    repeat(loop_test_for)(count)
    repeat(loop_test_for_in_list)(count)
    repeat(loop_test_for_allocate)(count)
    repeat(loop_test_while)(count)
    repeat(loop_test_while_allocate)(count)
    repeat(lambda n: [i for i in range(n)])(count)


# region str_tests
def str_test_f(str1: str, str2: str, str3: str):
    return f'str1: {str1}, str2: {str2}, str3: {str3}'


def str_test_format_no_number(str1: str, str2: str, str3: str):
    return 'str1: {}, str2: {}, str3: {}'.format(str1, str2, str3)


def str_test_format_with_number(str1: str, str2: str, str3: str):
    return 'str1: {0}, str2: {1}, str3: {2}'.format(str1, str2, str3)


def str_test_concat(str1: str, str2: str, str3: str):
    return 'str1: ' + str1 + ' str2: ' + str2 + ' str3: ' + str3


def str_test_join(str1: str, str2: str, str3: str):
    return ''.join(('str1: ', str1, ' str2: ', str2, ' str3: ', str3))
# endregion


# region loops

def loop_test_for(n=10000):
    arr = []
    for i in range(n):
        arr.append(i)
    return arr


def loop_test_for_in_list(n=10000):
    return [i for i in range(n)]


def loop_test_for_allocate(n=10000):
    arr = [0] * n
    for i in range(n):
        arr[i] = i
    return arr


def loop_test_while(n):
    arr = []
    i = 0
    while i < n:
        arr.append(i)
        i += 1
    return arr


def loop_test_while_allocate(n):
    arr = [0] * n
    i = 0
    while i < n:
        arr[i] = i
        i += 1
    return arr

# endregion



if __name__ == '__main__':
    main()
