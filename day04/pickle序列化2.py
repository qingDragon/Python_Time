import pickle

def sayhi(name):
    print("hello3",name)
info = {
    "name":"yanzhuang",
    "age":18,
    "func":sayhi
}
f = open("test.txt","wb")
# f.write(pickle.dumps(info))
pickle.dump(info,f) #完全等价于上面的语句

f.close()