name = "    Yanzhuang Yan  "
# print(name.count('ang'))
# print(name.capitalize())#首字母大写
# print(name.center(50, '*'))
# print(name.endswith("ng"))
# print(name.expandtabs(30))#将字符串中的\t转换成对应数量的空格
# name = "my name is {name},i am {year} year old"
# print(name.format(name="yanzhuang", year=8)) #格式化输出
# print(name.format_map({"name":"yanzhuang","year":8}))

# print(name.find("yan"))
# print(name.isdigit())
# name2 = "\t"
# print(name2.isalnum()) #不含特殊符号
# name2 = "abdcdjgflga"
# name3 = "123214"
# print(name2.isalpha())#全是纯英文字母
# print(name2.isdecimal())#是十进制
# print(name.isidentifier())#是不是合法的标识符
# print(name.islower())#是不是小写
# print(name.isnumeric())#都是数字，没啥用
print(name.isprintable())
print(name.isspace())#是不是空格
print(name.istitle())#是不是标题,每个单词首字母大写
print(name.isupper())#是不是大写
print("+".join(['1','2','3']))

print(name.ljust(50,"*"))#保证长度50，不够用*补在右面
print(name.rjust(50, "*"))#保证长度50，不够用*补在左面

print(name.lower())
print(name.upper())
print(name.lstrip())#去掉左边的空格
p = str.maketrans("abcdef","123456")
print(name.translate(p)) # 可以用在生成随机密码

print(name.replace('a','A',3)) #将a换成A，数字是换几个
print(name.rfind('a'))#返回最右边a的索引

print(name.split('a'))#返回列表

print(name.splitlines())#根据换行符来分割字符串

print(name.swapcase())#大小写互换
print(name.zfill(50))#从左往右补0，直至50位，16进制等使用