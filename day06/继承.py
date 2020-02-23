
class People(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print("%s is eating..."% self.name )
    def sleep(self):
        print("%s is sleeping..." % self.name)

class Man(People):
    def __init__(self,name,age,money):
        super(Man,self).__init__(name,age)
        self. money = money
    def sleep(self):
        People.sleep(self)
        print("man %s is sleeping..." % self.name)

p1 = People("YanZhuang",26)
p1.eat()
m1 = Man("GuYang",28,10)
m1.sleep()



