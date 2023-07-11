import logging
import os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

from faker import Faker

from timer import timer

cpuCount = os.cpu_count() * 2 + 1

fake = Faker()

bin_path = Path('bin')


def fake_handler(args):
    path, depth = args

    fake_path = fake.file_path(depth=depth, absolute=False)
    split_path = fake_path.split('/')
    dir_path = '/'.join(split_path[:-1])
    file_path = ''.join(split_path[-1:])

    if not Path(dir_path).exists():
        dest = path.joinpath(dir_path)
        dest.mkdir(parents=True, exist_ok=True)
        Path(f'{dest}/{file_path}').touch(exist_ok=True)


@timer
def create_bin(**kwargs):
    Faker.seed(0)

    args = [(kwargs['path'], kwargs['depth']) for i in range(kwargs['count'])]

    with ThreadPoolExecutor(max_workers=cpuCount) as executor:  # delta=0.018626125005539507
        executor.map(fake_handler, args)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    create_bin(path=bin_path, depth=5, count=100)
