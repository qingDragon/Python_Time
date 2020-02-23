import shutil


with open("yesterday.txt","r",encoding = "utf-8") as f,\
    open("yesterday2.txt","w",encoding = "utf-8") as f2:
    shutil.copyfileobj(f,f2)


shutil.copyfile("yesterday2.txt","ad.bak")
