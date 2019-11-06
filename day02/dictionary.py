info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya",
}


info["stu1104"] = "苍井空"

print(info)

info["stu1101"] = "武藤兰"
print(info)
#
# info.pop("stu1101")#标准删除方式
# print(info)

# del info["stu1103"]#换个姿势
# print(info)

info.popitem()#随机删除? 从右边开始删

print(info)

print("stu1102" in info)#标准用法

#获取
print(info.get("stu1102"))
print(info.get("stu1104"))
# print(info["stu1104"]) #不存在key就会报错，get方法不会出现，不存在的显示“none”

print(info.values())
print(info.keys())
print(info.setdefault("stu1103","yanzhuang"))
print(info)

b = {
    1:2,
    3:4,
    'stu1102':'泷泽萝拉'
}
info.update(b)
print(info)

#转换成列表
print(info.items())
#初始化一个字典
c = dict.fromkeys([1,2,3],'test')
print(c)
#有坑:存在多级value时，该一个就全部更改，是由于是同一块内存地址
c = dict.fromkeys([1,2,3],[1,2,"test"])
print(c)
c[1][2] = "test----"
print(c)

#循环（常用，效率高）
for key in info:
    print(key, info[key])
#循环2
for k,v in info.items():#先把dict转成list，数据量大影响执行效率
    print(k, v)