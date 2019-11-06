
user = "yanzhuang"
pwd = "abc123"
def auth(authtype):
    print("auth:",authtype)
    def out_wapper(func):
        def wapper(*args, **kwargs):
            if authtype == "local":
                username = input("username:")
                password = input("password:")
                if user == username and pwd == password:
                    print("User passed authentication")
                    res = func(*args, **kwargs)
                    print("------after anthentication----")
                    return res
                else:
                    exit("invalid username or password")
            elif authtype == "ldop":
                print("my mbp is coming")
        return wapper
    return out_wapper
@auth(authtype = "local")
def index():
    print("welcome to index page")
@auth(authtype="local")
def home():
    print("welcome to home page")
    return "from home"
@auth(authtype = 'ldop')
def bbs():
    print("welcome to bbs page")

index()
print(home())
bbs()
