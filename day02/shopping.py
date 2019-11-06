'''
1、启动程序后，让用户输入工资，然后打印商品列表
2、允许用户根据商品编号购买物品
3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
4、可随时退出，退出时打印已购买商品和余额
'''

salary = int(input("please input your salary:"))
print(salary)

goods_list = [["洗衣液", 20], ["毛巾", 10], ["牙刷", 10], ["笔记本", 5], ["剃须刀", 50]]
print(goods_list)
goods_list2 = []#存放已购买物品清单

while True:
    #判断金额是否大于0
    if salary <= 0 :
        print("您的余额不足")
        break;
    else:
        print('''
        1、洗衣液 20
        2、毛巾 10
        3、牙刷 10
        4、笔记本 5
        5、剃须刀 50
        ''')
        #金额满足要求后输入商品编号
        id = input("please input goods number:(按b退出）")
        if id == "b":
            break;
        id_int = int(id)-1 #转换id为int类型
        # 判断商品编号是否合法
        if id_int >= 0:
            #判断工资是否购买已选商品
            if salary >= goods_list[id_int][1]:
                salary = salary - goods_list[id_int][1]
                goods_list2.append(goods_list[id_int][0])
            else:
                print("您的余额不足,余额%d元" %salary)
                break;
        else:
            #非法输入商品编号
            print("您的输入有误！请重新输入")
            continue;
print("您已购买：", goods_list2)
print("您的余额为：",salary)
