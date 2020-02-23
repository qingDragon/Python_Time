

class Dog(object):
    name = "12"
    def __init__(self,name):
        self.name = name
    @staticmethod #实际上跟类没有什么关系了,名义上归类管
    def eat(self,food):
        print("%s is eating %s" %(self.name,food))



d = Dog("guyang")
d.eat(d,"jll")