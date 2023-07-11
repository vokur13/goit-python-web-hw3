import logging
from pathlib import Path

from timer import timer

p = Path('bin')


@timer
def parse(path):
    if path.exists():
        for i in path.iterdir():
            if i.is_dir():
                parse(i)
            elif i.is_file():
                dest = p.parent.joinpath('dest').joinpath(i.suffix[1:])
                if not dest.exists():
                    dest.mkdir(parents=True, exist_ok=True)
                i.rename(dest.joinpath(i.name))
        for i in path.iterdir():
            if not any(i.iterdir()):
                i.rmdir()
        path.rmdir()
    else:
        logging.info(f'No {path=} found')


@timer
def clean(path):
    for i in path.iterdir():
        if not any(i.iterdir()):
            i.rmdir()
    path.rmdir()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    parse(p) # delta=0.04296233301283792
