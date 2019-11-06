

def fab(max):
    n,a,b = 0,0,1
    while n < max:
        yield(b)
        a,b = b,a+b
        n +=1
    return "done"
f = fab(10)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
#超过数量后，抛出异常，异常信息就是return返回值
print(f.__next__())
