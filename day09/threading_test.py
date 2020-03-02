

import threading
import time

def run(n):
    print("task", n)
    time.sleep(2)

start_time = time.time()
t_objs = []
for i in range(50):
    t = threading.Thread(target=run,args=("t%s"%i,))
    t.setDaemon(True) #设置为守护线程
    t.start()
    t_objs.append(t)
#
# for t in t_objs:
#     t.join()

print("cost:%s" %(time.time()-start_time), threading.activeCount())
#你以为别人都和你一样啊，屌丝没有生活