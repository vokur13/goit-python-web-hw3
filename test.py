import logging
import os
from pathlib import Path

from timer import timer

from faker import Faker

fake = Faker()


@timer
def fake_handler(n: int):
    path = Path('bin')

    current_dir = Path().absolute()

    logging.info(f'Before: {current_dir=}')

    fake_path = fake.file_path(depth=2, absolute=False)
    split_path = fake_path.split('/')
    dir_path = '/'.join(split_path[:-1])
    file_path = ''.join(split_path[-1:])

    if not Path(dir_path).exists():
        # logging.info(f'{path_info=}')

        dest = path.joinpath(dir_path)
        dest.mkdir(parents=True, exist_ok=True)
        Path(f'{dest}/{file_path}').touch(exist_ok=True)

        #
        # os.chdir(str(dest))
        # logging.info(f'Middle: {Path().absolute()=}')
        # Path(file_path).touch(exist_ok=True)

    os.chdir(str(current_dir))
    logging.info(f'After: {Path().absolute()=}')
    logging.info(f'{n=}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    fake_handler(1)
