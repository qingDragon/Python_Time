import time
from urllib import request
from gevent import monkey
import gevent

monkey.patch_all() #把当前程序中的IO操作打上标记

def f(url):
    print("GET: %s" %url)
    resp = request.urlopen(url)
    data = resp.read()
    print("%d bytes received from %s" %(len(data),url))

urls = [
    'https://www.python.org/',
    'https://www.yahoo.com/',
    'https://www.github.com/'
]
time_start = time.time()
for url in urls:
    f(url)
print("同步cost",time.time() - time_start)

async_time_start = time.time()
gevent.joinall([
    gevent.spawn(f,urls[0]),
    gevent.spawn(f,urls[1]),
    gevent.spawn(f,urls[2])
])
print("异步cost",time.time()- async_time_start)