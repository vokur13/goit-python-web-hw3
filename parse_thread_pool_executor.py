import os
from concurrent.futures import ThreadPoolExecutor
import logging
from pathlib import Path

from timer import timer

cpuCount = os.cpu_count() * 2 + 1

p = Path('bin')


def iterate(i):
    if i.is_dir():
        parse(i)
    elif i.is_file():
        dest = p.parent.joinpath('dest').joinpath(i.suffix[1:])
        if not dest.exists():
            dest.mkdir(parents=True, exist_ok=True)
        i.rename(dest.joinpath(i.name))


def clean(i):
    if not any(i.iterdir()):
        i.rmdir()


@timer
def parse(path):
    if path.exists():
        for i in path.iterdir():
            with ThreadPoolExecutor(max_workers=cpuCount) as executor:  # delta=0.07156820798991248
                executor.submit(iterate, i=i)
        for i in path.iterdir():
            with ThreadPoolExecutor(max_workers=cpuCount) as executor:  # delta=0.07156820798991248
                executor.submit(clean, i=i)
        path.rmdir()
    else:
        logging.info(f'No {path=} found')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    parse(p)
