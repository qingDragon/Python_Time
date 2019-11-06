# names = ["zhangshuo", "guyang", "yanzhuang", ["guyang", "zhangshuo"]]
# names2 = names.copy()
#
# print(names)
# print(names2)
#
# names[2] = "yz"
#
# print(names)
# print(names2)
#
# names2[3][0] = "gy"
# print(names)
# print(names2)
import copy
names = ["zhangshuo", "guyang", "yanzhuang", ["guyang", "zhangshuo"]]
names2 = copy.deepcopy(names)

names[3][0] = "gy"

print(names)
print(names2)

for i in names:
    print(i)
