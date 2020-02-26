



# mod = __import__('lib.aa') #python解释器内部使用的，不建议使用
#
# obj = mod.aa.C()
# print(obj.name)



import importlib

aa = importlib.import_module('lib.aa')
print(aa.C().name)