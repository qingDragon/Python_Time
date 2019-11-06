

with open("yesterday.txt","r",encoding="utf-8") as f,\
    open("yesterday_new.txt","w",encoding="utf-8") as f_new:
    for line in f:
        if "when I was young" in line:
            line = line.replace("when I was young", "----------WHEN YAN WAS YOUNG-----------")
        f_new.write(line)