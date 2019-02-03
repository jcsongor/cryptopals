from contextlib import contextmanager
import time


@contextmanager
def timer(label: str = ''):
    start = time.time()
    yield
    end = time.time()
    print('%s finished in %f seconds.' % (label, end - start))
