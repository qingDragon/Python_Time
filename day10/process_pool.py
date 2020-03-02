import os
import time
from multiprocessing import Pool

def Foo():
    time.sleep(2)
    print("in the process ",os.getpid())

def Bar(arg):
    print("--->exec done:",arg,os.getpid())

if __name__ == "__main__":

    pool = Pool(processes=3) #允许进程池里同时放入3个进程
    for i in range(10):
        # pool.apply(func=Foo,args=(i,))#串行
        pool.apply_async(func=Foo,args=(i,),callback=Bar)
    print('end')
    pool.close() #一定要先close，再join，不然程序就直接结束了
    pool.join()