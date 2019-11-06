
# #Return True if all elements of the iterable are true (or if the iterable is empty)
# print(all([1, 2, 3,  0]))
# #Return True if any element of the iterable is true. If the iterable is empty, return False.
# print(any([1,0]))
#
# print([ascii([1,2,"开外挂"])])#没什么用
#
# bin(2)#十进制转二进制
#
# bool() #判断真假
#
# bytearray()#可以修改
# b = bytearray("abcde", encoding='utf-8')
# print(b[2])
# b[2]= 100
# print(b)
# a = bytes("abcde", encoding='utf-8')
# print(a.capitalize(), a)#字符串不能修改，二进制字节格式也不能修改，只能覆盖

# def tt():
#     pass
# print(callable(tt)) #后面可以加括号的就可以调用，返回true

# chr(98) #数字转为ascii对应的字符
#
# ord('b')#ascii对应的字符转换为数字
#
#
# compile()#基本用不到


# code = '''
# def fab(max):
#     n,a,b = 0,0,1
#     while n < max:
#         yield(b)
#         a,b = b,a+b
#         n +=1
#     return "done"
# f = fab(10)
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# '''
#
# py_obj = compile(code,'err.log','exec')#中间的参数是用来写入日志的
#
# exec(py_obj)
# exec(code) #也可以执行


# dir()#查询可以调用的方法
#
# eval()#字符串变成字典，有语句的用exec
#
# filter()#一组数据中过滤想要的


# res = filter(lambda n:n>5,range(10))
# res = map(lambda n:n*n,range(10))  #等价于[i*2 for i in range(10)]
# for i in res:
#     print(i)

#匿名函数
# (lambda n:print(n))(5)
# calc = lambda n:print(n)  #lamda处理不了复杂的语句，比如for循环
# calc(5)



# import functools#3.0中reduce在标准库里
#
# res = functools.reduce(lambda x,y:x+y,range(10))
#
# print(res)#累加，还可以阶乘，x,y:x*y


# a = frozenset([1,22,4,56,33,4,2,4,2])#不可变集合，不可以增删改

# print(globals())#返回当前程序里所有的全局变量的键值对

# hash()#散列 ：生成一个映射
#
# hex()#数字转成16进制

# def test():
#     a = 333
#     print(locals())
# test()
# print(locals())#与globals()比，可以在函数中使用，打印函数作用域局部变量键值对


# oct()#转8进制
#
# pow(3,5)#3的5次方
#
# repr(object)#用字符串表示一个对象
#
#
# round(1.3342,2) #将前面的小数保留两位小数



#sort()
# a = {6:2,8:0,1:4,-5:6,99:11,4:22}
# print(sorted(a.items(),key = lambda x:x[0]))#转换成列表排序




# zip()
#
#
# a = [1, 2, 3, 4, 5, 6]
#
# b = ['a', 'b', 'c', 'd']
# for i in zip(a,b):#按最小数量拼
#     print(i)
#



# import decorator
# __import__("decorator") #只知道模块的字符串，引用模块