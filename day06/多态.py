

class Animal(object):
    def __init__(self,name):
        self.name = name

    def talk(self):
        pass

    @staticmethod
    def animal_talk(obj):
        obj.talk()
class Dog(Animal):
    def talk(self):
        print("wangwang")
class Cat(Animal):
    def talk(self):
        print("miaomiao")
def animal_talk(obj):
    obj.talk()
d = Dog("os")
c = Cat("sb")

Animal.animal_talk(d)
Animal.animal_talk(c)