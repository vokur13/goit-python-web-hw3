import logging
import os
from pathlib import Path

from faker import Faker

from timer import timer

cpuCount = os.cpu_count() * 2 + 1

fake = Faker()

bin_path = Path('bin')


def fake_handler(path: Path = bin_path, depth: int = 3):


    fake_path = fake.file_path(depth=depth, absolute=False)
    split_path = fake_path.split('/')
    dir_path = '/'.join(split_path[:-1])
    file_path = ''.join(split_path[-1:])

    if not Path(dir_path).exists():
        dest = path.joinpath(dir_path)
        dest.mkdir(parents=True, exist_ok=True)
        Path(f'{dest}/{file_path}').touch(exist_ok=True)


@timer
def create_bin(path=bin_path, depth=3, count: int = 10):
    Faker.seed(0)
    folder_count = 0
    for _ in range(count):
        fake_handler(path, depth)
        folder_count += 1
    logging.info(f'{folder_count=}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')

    create_bin(path=bin_path, depth=5, count=100)  # delta=0.02259616699302569
