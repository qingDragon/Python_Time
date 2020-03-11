from greenlet import greenlet
#协程里的手动挡，gevent是更上层的封装，自动档
def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()


def test2():
    print(56)
    gr1.switch()
    print(78)

gr1 = greenlet(test1) # 启动一个协程
gr2 = greenlet(test2)
gr1.switch()


