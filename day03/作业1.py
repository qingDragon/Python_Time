

#实现简单的shell sed替换功能


f = open("yesterday.txt","r",encoding="utf-8")
f_new = open("yesterday_new.bak", "w", encoding="utf-8")

for line in f:
    if "when I was young" in line:
        line = line.replace("when I was young","----------WHEN I WAS YOUNG-----------")
    f_new.write(line)

f.close()
f_new.close()