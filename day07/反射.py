

def bulk(self):
    print("%s is yelling"%self.name)
class Dog(object):

    def __init__(self,name):

        self.name = name

    def eat(self,food):
        print("%s is eating %s" %(self.name,food))

d = Dog("guyang")
choice = input(">>:").strip() #根据用户输入的字符串调用对应方法

if hasattr(d,choice):
    func = getattr(d,choice)
    func("zhangshuo")
else:
    setattr(d,choice,bulk) #通过字符串动态给实例装配外部方法

d.talk(d)


# print(hasattr(d,choice)) #反射看看有没有这个属性
#
# getattr(d,choice)() #通过getaddr调用