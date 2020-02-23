class YzException(Exception):
    def __init__(self,msg):
        self.message = msg
    # def __str__(self):
    #     return "123213"

try:
    raise YzException("数据库连不上") #触发自己的异常
except YzException as e:
    print(e)
