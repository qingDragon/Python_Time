name=input("name:")
age= input("age:")
job = input("job:")
salary = input("salary:")


info = '''
-------- info of {_name} -------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
'''.format(_name = name, _age = age, _job = job, _salary = salary )

info2 = '''
--------info of {0} ------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
'''.format(name,age,job,salary)
# print (info)

info3='''
--------info of %s ------
Name:%s
Age:%s
Job:%s
Salary:%s
''' %(name,name,age,job,salary)

print(info3)