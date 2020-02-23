

class Dog(object):
    name = "12"
    def __init__(self,name):
        self.name = name
        self.__food = None #私有属性

    @property #把一个方法编程静态属性，不能传参数了
    def eat(self):
        print("%s is eating %s" %(self.name,self.__food))

    @eat.setter
    def eat(self, food):
        print("set to food", food)
        self.__food = food

    @eat.deleter
    def eat(self):
        del self.__food
        print("删完了")




d = Dog("guyang")
d.eat
#设置属性
d. eat = "baozi"
d.eat

del d.eat
d.eat
