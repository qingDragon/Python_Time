import time

print(time.altzone)
print(time.asctime())
print(time.localtime()) #返回本地时间的struct time模式
print(time.gmtime()) #返回utc时间的struct time模式
print(time.asctime(time.localtime()))

print(time.ctime())

string_2_struct = time.strptime("2016/05/22","%Y/%m/%d")#将日期字符串转成struct time时间对象格式
print(string_2_struct)

struct_2_stamp = time.mktime(string_2_struct)#将struct时间对象转成时间戳
print(struct_2_stamp)

print(time.gmtime(time.time()))#将utc时间戳转换成struct_time格式
print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()))#将utc struct_time转换成指定的字符串格式

