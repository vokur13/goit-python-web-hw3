import logging
from multiprocessing import Pool, cpu_count
from timeit import default_timer

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def factorize(*args):
    for arg in args:
        return [i for i in filter(lambda x: arg % x == 0, range(1, arg + 1))]


if __name__ == '__main__':
    t1 = default_timer()
    with Pool(processes=cpu_count()) as pool:
       result=pool.map(factorize, (128, 255, 99999, 10651060))
    a, b, c, d = result
    t2 = default_timer()
    delta = t2 - t1  # delta=0.5267880000174046
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
