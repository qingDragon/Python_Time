#商家入口

f = open("shopping_list.txt")
choice = input("选择更改价格的商品：")
shopping_list = []
if choice.isdigit():
    choice = int(choice)
    #读取文件，生成商品列表
    for line in f:
        shopping_list.append(line)
    f.close()
    # print(shopping_list)
    # print(shopping_list[choice])
    #选择要更改的商品
    str_choice = shopping_list[choice]
    new = input("请输入新的价格：")
    if new.isdigit():
        new = int(new)
        #将更改后的商品字符串重新赋给列表
        shopping_list[choice]=str_choice[:str_choice.index(" ")]+" "+str(new)+"\n"
        print("您已修改成功，新的价格为：",shopping_list[choice])
    #将新的商品列表写入原来的文件
    f = open("shopping_list.txt","w")
    for i in shopping_list:
        f.write(i)
    f.close()
