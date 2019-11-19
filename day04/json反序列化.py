# import json
# f = open("test.txt","r")
#
# data = json.loads(f.read())
# print(data.get("name"))
#
# f.close()


import pickle
data = {'k1':123,'k2':'hello'}
#pickle.dumps 将数据通过特殊的形式转换为只有python认识的字符串
p_str = pickle.dumps(data)
print(p_str)

print(type(data))
#pickle.dump 将数据通过特殊的形式转换为只有python认识的字符串，并写入文件
with open("test.pk",'w') as f:
    #python3会报错，python3中文件写入模式应为“wb”，使用二进制方式，而不是字符方式写入
    pickle.dump(data,f)

import json

j_str = json.dumps(data)
print(j_str)

#json.dump 将数据通过特殊的形式转换为所有程序语言都认识的字符串，并写入文件
with open("test.json","w") as f:
    json.dump(data,f)



