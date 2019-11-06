
 # 输入用户名密码
 # 认证成功后显示欢迎信息
 # 连续输错三次后锁定
count = 0
while True:
    #输入用户名密码
    username = input("Username:")
    password = input("Password:")
    #打开用户名密码文件
    f = open('login_true.txt')
    #打开锁定用户名文件
    f4 = open('login_lock.txt')
    #判断输入用户名是否存在于锁定文件中
    for line in f4:
        user_name2 = line.strip()
        if username == user_name2:
            print("username is locked!")
            break
    else:
        #判断用户名密码是否正确
        for line in f:
            str = line.strip()
            str2 = ','
            user_name = str[:str.index(str2)]
            pass_word = str[str.index(str2)+1:]
            # print(user_name, pass_word)
            #用户名密码均正确，打印欢迎信息并清空计数器跳出循环
            if username == user_name and password == pass_word:
                print("welcome " + username)
                count = 0
                break
            #用户名正确，密码错误，打印提示信息，计数器加1，并判断计数器是否到3
            elif username == user_name and password != pass_word:
                print("wrong password!")
                count += 1
                print(count)
                #计数器到达3次，将用户名写入锁定文件中
                if count == 3:
                    f2 = open('login_lock.txt', "a+")
                    f2.write(username+'\n')
                    f2.close()
                    count = 0

                break
        else:
            print("please check out your username!")
            count = 0
        f.close()