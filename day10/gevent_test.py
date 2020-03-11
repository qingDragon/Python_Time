
import gevent
#自动挡，遇到io操作自动切换
def fun1():
    print("running fun1")
    gevent.sleep(2)
    print("running fun1 again")

def fun2():
    print("running fun2")
    gevent.sleep(1)
    print("running fun2 again")

def fun3():
    print("running fun3")
    gevent.sleep(0)
    print("runing fun3 again")

gevent.joinall([
    gevent.spawn(fun1),
    gevent.spawn(fun2),
    gevent.spawn(fun3)
])