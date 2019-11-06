
#函数嵌套：在一个函数体内定义另外一个函数
def foo():
    print('in the foo')

    def bar():#类似局部变量的作用
        print("in the bar")

    bar()

foo()



