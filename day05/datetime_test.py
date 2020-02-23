import datetime
import time

print(datetime.datetime.now())
print(datetime.date.fromtimestamp(time.time())) #时间戳直接转换成日期格式

print(datetime.datetime.now())
print(datetime.datetime.now()+datetime.timedelta(3)) #当前时间+3天
print(datetime.datetime.now()+datetime.timedelta(-3)) #当前时间-3天
print(datetime.datetime.now()+datetime.timedelta(hours = 3))
print(datetime.datetime.now()+datetime.timedelta(minutes=30))


c_time = datetime.datetime.now()
print(c_time.replace(minute=3,hour=2))