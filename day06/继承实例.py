class School(object):
    def __init__(self,name):
        self.name = name

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course

    def teach(self):
        pass

class Student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade):
        super(SchoolMember,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade
        


