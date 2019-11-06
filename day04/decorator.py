

import time

def timer(func):
    def deco(*args,**kwargs):#增加可变参数，灵活调用
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print("the func run time is %s" %(end_time - start_time))
    return deco
@timer # 相当于test1 = timer(test1)
def test1():
     time.sleep(3)
     print("in the test1")

@timer
def test2(name):
    print("test2:",name)
test1()
test2("yanzhuang")
# deco(test1) #实现了附加功能但是改变了函数的调用方式

