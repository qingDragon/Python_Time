

def test1():
    def test2():
        print("in the test2")
        return 1
    return test2

print(test1())#执行test1返回的是test2的内存地址