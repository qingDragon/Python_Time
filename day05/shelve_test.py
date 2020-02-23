import datetime
import shelve


#对pickle更上一层的封装
#是一个简单的k,v将内存数据通过文件持久化的模块，
# 可以持久化任何pickle可支持的python数据格式

d = shelve.open('shelve_test')#打开一个文件

info = {
    'age':22,
    "job":"it"
}

name = ["alex","rain","test"]
d["name"] = name
d["info"] =info
d["date"] = datetime.datetime.now()
d.close()