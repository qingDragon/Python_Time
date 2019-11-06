

def fab(max):
    n,a,b = 0,0,1
    while n < max:
        #print(b)
        yield(b)
        a,b = b,a+b
        n +=1
    return "done"
f = fab(10)
print(type(f))