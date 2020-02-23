
class Role:
    n = 123 #类变量
    n_list = []

    name = "我是类变量"
    def __init__(self, name, role, gun, money =15000, hp =100):
        self.name = name #实例变量（静态属性），作用域是实例本身
        self.role = role
        self.gun = gun
        self.money = money
        self.__hp = hp #私有属性，可以定义方法进行访问

    def got_shot(self): #类的方法（动态属性）
        print("i am got shot....")

    def buy_gun(self,gun_name):
        print("%s buy gun %s" %(self.name,gun_name))

    def __shot(self): #私有方法
        print("shot....")

r1 = Role("yz","police","ak47")
r1.n_list.append("in r1")
r1.bullet_prove = True #可以给实例增加属性
r2 = Role("gy","terrist","b22")
r2.n_list.append("in r2")
r1.buy_gun("ak47")
r1.n = "在实例变量中修改"

del r1.gun

print(r1.n,r2.n,r1.name,r1.bullet_prove) #实例变量和类变量同名，先去实例变量里面找，然后去类变量里找，同名的话，默认去实例变量里
print(Role.n_list,r1.n_list)



print(r1.__hp)