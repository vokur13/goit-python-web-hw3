import logging
from timeit import default_timer


def factorize(*args):
    res = []
    for arg in args:
        res.append([i for i in filter(lambda x: arg % x == 0, range(1, arg + 1))])
    return res


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    t1 = default_timer()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    t2 = default_timer()
    delta = t2 - t1  # delta=0.4715305000427179
    logging.info(f'RunTime: {delta=}')

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]

    print(f'{a=}')
    print(f'{b=}')
    print(f'{c=}')
    print(f'{d=}')
