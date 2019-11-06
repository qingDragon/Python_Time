import pickle

def sayhi(name):
    print("hello",name)
info = {
    "name":"yanzhuang",
    "age":22,
    "func":sayhi
}
f = open("test.txt","wb")
f.write(pickle.dumps(info))
f.close()