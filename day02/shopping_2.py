
#新建商品列表
product_list = [
    ('iphone', 4500),
    ('macbook', 9800),
    ('bicycle', 200),
    ('coffee', 31),
    ('《巴比龙》', 21),
    ('guitar', 3500)
]
#新建空的购物车列表
shopping_list = []
#用户输入salary，判断是否是整数
salary = input("input your salary:")
if salary.isdigit():
    salary = int(salary)
    #循环打印商品列表，并询问用户是否购买，可随时退出
    while True:
        #循环打印列表，商品编号与商品成对打印
        for index,item in enumerate(product_list):
            print(index, item)
        #询问用户是否购买
        user_choice = input("选择要买吗?>>>:")
        #判断用户输入的商品编号是否合法
        if user_choice.isdigit():
            user_choice = int(user_choice)
            #判断用户输入的商品编号是否包含在商品列表中
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                #判断选择的商品价格是否能够支付
                if p_item[1] <= salary:
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print('Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m ' %(p_item,salary))
                else:
                    print("\033[41;1m您的余额买不了此商品，还买个屁啊\033[0m")
            else:
                print("procduct code [%s] is not exist!"% user_choice)
        elif user_choice == 'q':
            #输入'q'：打印已买商品列表和余额并退出程序
            print('---------shopping list---------')
            for p in shopping_list:
                print(p)
            print("your current balance is:",salary)
            exit()
        else:
            print('invalid option')
else:
    print("invalid salary input")
    exit()