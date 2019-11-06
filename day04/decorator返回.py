#原函数有返回值
import time
def timer(func):
    def deco(*args,**kwargs):#增加可变参数，灵活调用
        start_time = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        print("the func run time is %s" %(end_time - start_time))
        return res
    return deco
@timer # 相当于test1 = timer(test1)
def test1():
     print("in the test1")
     return "from test1"

test1()

print(test1())
