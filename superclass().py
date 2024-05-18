class Human:
    def __init__(Self,name,age):
        Self.name=name
        Self.age=age
    def printDetails(Self):
        print(f'Name is{Self.name}')
        print(f'Age is{self.age}')
class Employee(Human):
    def __init__(Self,name,age,eid,sal):
        super(). __init__(name,age)
        Self.eid=eid
        Self.sal=sal
    def printDetails(Self):
        super().printDetails()
        print(f'eid is {Self.eid}')
        print(f'sal is {Self.sal}')
class Student(Human):
    def __init__(self,name,age,sid,course,college):\
        super().__init__(name,age)
        Self.sid=sid
        Self.course=Course
        Self.college=college
    def printDetails():
             print(f'sid is {self.sid}')
             print(f'course is {self.course}')
             print(f'college is {self.college}')
             
e=Employee('priyanka',24,1024,25000)
e.printDetails()

s=Student('zini',24,'102423','xyzcollege')
s.printDetails
  