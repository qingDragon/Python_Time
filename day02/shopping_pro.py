#购物车
#用户入口：
#1、商品信息存在文件里
#2、已购商品，余额记录
#商家入口：
#可以添加商品，修改价格

import os
f = open("shopping_list.txt")
f2 = open("shopping_record.txt","r+")
shopping_list = [] #从文件中获取的商品列表
shopping_cart = [] #已购商品清单
#从文件中读取，生成商品列表
for line in f:
    str_line = line.strip()
    shopping_list.append(str_line.split(" "))
# print(shopping_list[0][1])

#判断是否第一次进入，是就让用户输入余额，否则从文件(shopping_record.txt)中获取余额
if os.path.getsize("shopping_record.txt") == 0:
    salary = input("请输入余额：")
else:
    # print("salary is")
    # print(os.path.getsize("shopping_record.txt"))
    for line2 in f2:
        str_line2 = line2.strip()

    salary = str_line2[str_line2.index("-")+1:]
    print("您已有购买记录，余额%s"%salary)


#用户购买商品，按q退出
if salary.isdigit():
    salary = int(salary)
    while True:
        print(shopping_list)
        user_choice = input("请选择是否购买：")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice >=0 and user_choice < len(shopping_list):
                if salary >= int(shopping_list[user_choice][1]):
                    shopping_cart.append(shopping_list[user_choice])
                    salary -= int(shopping_list[user_choice][1])
                    print("已将%s添加购物车,余额还剩%s " % (shopping_list[user_choice], salary))
                else:
                    print("余额只剩%s,还买个屁啊" % salary)
            else:
                print("没有此商品")

        elif user_choice =="q":
            print("-------------you buy-----------")
            for p in shopping_cart:
                print(p)
            #将购买记录写入文件shopping_record.txt
            if len(shopping_cart)!=0:
                str_write = str(shopping_cart)+"-"+str(salary)
                f2.write(str_write+'\n')
            f.close()
            f2.close()
            print("your current balance is %s" %salary)
            exit()
            #退出打印
