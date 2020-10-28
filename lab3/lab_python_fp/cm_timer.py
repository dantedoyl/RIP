import time
from contextlib import contextmanager

class cm_timer_1:

    def __init__(self):
        self.before_time = 0
        self.after_time = 0

    def __enter__(self):
        self.before_time = time.perf_counter()
        # Должен возвращаться значимый объект
        # например, открытый файл
        return time.perf_counter()

    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            self.after_time = time.perf_counter()
            print('time: {}'.format(round(self.after_time-self.before_time, 2)))

@contextmanager
def cm_timer_2():
    before_time = time.perf_counter()
    yield time.perf_counter()
    after_time = time.perf_counter()
    print('time: {}'.format(round(after_time - before_time,2)))

# with cm_timer_1():
#     time.sleep(2.5)
#
# with cm_timer_2():
#     time.sleep(2.5)