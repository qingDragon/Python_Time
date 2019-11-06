#sys模块两个方法

# import sys

# print(sys.argv)
# print(sys.argv)
# print(sys.path)


# import os
# # os.system("dir")
# # cmd_res = os.system("dir")
# # print("->", cmd_res)
#
# cmd_res = os.popen("dir").read()
# print("->", cmd_res)

str = "我爱北京天安门"

print(str.encode(encoding='utf-8'))
print(str.encode(encoding='utf-8').decode(encoding='utf-8'))