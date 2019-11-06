

import time

def consumer(name):
    print("%s 准备吃包子了" % name)
    while True:
        baozi = yield
        print("包子[%s]来了，被[%s]吃掉了" %(baozi, name))

def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("%s 开始做包子了" % name)
    for i in range(10):
        time.sleep(1)
        print("做了1个包子，分了两半")
        c.send(i)   # 给yield传值并继续执行yield下面的语句
        c2.send(i)
producer("yanzhuang")