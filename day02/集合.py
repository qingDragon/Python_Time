list = set([1, 2, 3, 4, 8])
print(list, type(list))
list_2 = set([1,3,4,7,8,98,43])
list_3 = set([1,2,3,4,8,7,9])
print(list.intersection(list_2))
print(list & list_2)#交集

print(list.union(list_2))
print(list | list_2)#并集

print(list.difference(list_2))
print(list-list_2)#在list中不在list_2中

print(list_2.difference(list))
print(list_2-list)

print(list_2.issubset(list_3))
print(list2 <= list_3) #list_2是不是list_3的子集

print(list_3.issuperset(list))
print(list_3 >= list) #父集

print(list.symmetric_difference(list_3))
print(list ^ list_3)#对称差集


list = set([3, 5, 9, 10])
list2 = set("hello")

list.add(2)
list2.add('H')

print(list)
print(list2)

list.remove(2) #remove没有的元素会报错

print(len(list))

print(3 in list)#测试是否是成员
print(2 not in list)

print(list.copy()) #返回一个list的浅copy
list_2 = set([0,4])
print(list.isdisjoint(list_2))#判断有没有交集，没有就返回ture



list.update([34,232,12]) #添加多项
print(list)

#删除
print(list.pop()) #返回随机删除的一项

print(list.discard(23)) #需要制定要删除的元素，如果没有该元素，返回none，不会报错


