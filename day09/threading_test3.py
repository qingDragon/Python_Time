# -*-coding:utf-8-*-

import threading
import time

def run(n):
    # lock.acquire() #获取锁
    global num
    num+= 1
    time.sleep(2)
    # lock.release() #释放锁
# lock = threading.Lock()
start_time = time.time()
t_objs = []
num = 0
for i in range(1000):
    t = threading.Thread(target=run,args=("t%s"%i,))
    t.start()
    t_objs.append(t)
#
# for t in t_objs:
#     t.join()

print("cost:%s" %(time.time()-start_time),num )
#你以为别人都和你一样啊，屌丝没有生活