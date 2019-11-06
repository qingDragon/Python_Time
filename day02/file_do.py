# f_read = open('yesterday.txt',encoding='utf-8').read()
# print(f_read)


# f= open('yesterday.txt',encoding = 'utf-8')
# first_line = f.readline()
# print(f.tell())
# print(first_line)
# data = f.read()
# print("----------------------")
# print(data)
#
# f.close()

# print(f.readline())
# print(f.tell())
# f.seek(0)
# print(f.tell())
# print(f.readline())

f = open('yesterday2.txt', 'r+', encoding='utf-8')

print("first:", f.readline())
print("second:", f.readline())
print("third:", f.readline())
f.write("\n3我爱北京天安门\n")
f.write("3天安门上太阳升")

print(f.tell())
f.seek(0)
f.write("\n北京欢迎你a")#有内容的情况下，不能从头写，会出现错误
f.close()


