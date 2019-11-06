import pickle

def sayhi(name):


    print("hello2", name)
f = open("test.txt","rb")

data = pickle.loads(f.read())#等价于data = pickle.load(f)
print(data["func"]("yanzhuang"))

f.close()