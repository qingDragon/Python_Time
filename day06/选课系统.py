
#学校
class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.teachers = []
        self.courses = []
        self.grades = []

    #学员注册
    def enroll(self,stu_obj):
        print("为学员%s办理注册手续" %stu_obj.name)
        self.students.append(stu_obj)
    #雇佣老师
    def hire(self,tea_obj):
        print("雇佣新老师%s" % tea_obj.name)
        self.teachers.append(tea_obj)
    #创建课程
    def create_course(self,course_type,price,time):
        print("%s学校创建了课程[%s]" % (self.name, course_type))
        self.courses.append(Course(course_type,price,time))
    #创建班级
    def create_grade(self,grade_name,course,teacher):
        print("%s学校创建了班级[%s]" %(self.name, grade_name))
        self.grades.append(Grade(grade_name,course,teacher))
#班级类
class Grade(object):
    def __init__(self,grade_name,course,teacher):
        self.grade_name = grade_name
        self.course = course
        self.teacher = teacher

#讲师类
class Teacher(object):
    pass

#学员类
class Student(object):
    pass
#课程类
class Course(object):
    def __init__(self,type,price,time):
        self.type = type
        self.price = price
        self.time = time