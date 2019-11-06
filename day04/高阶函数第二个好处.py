#不改变函数的调用
import time

def bar():
    time.sleep(3)
    print("in the bar")

def test1(func):
    print(func)
    return func

# print(test1(bar))

# t = test1(bar)
# t()


bar = test1(bar)
bar()