import threading
import time


class MyThread(threading.Thread):

    def __init__(self, func, args=()):
        super(MyThread, self).__init__()

        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None


def foo(a, b, c):
    time.sleep(1)
    return a * 2, b * 2, c * 2


st = time.time()
li = []
for i in range(4):
    t = MyThread(foo, args=(i, i + 1, i + 2))
    li.append(t)
    t.start()
for t in li:
    t.join()
    print(t.get_result())

et = time.time()
print(et - st)
