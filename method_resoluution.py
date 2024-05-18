# class A:pass
# class B(A):pass
# class C(A):pass
# class D(B):pass
# class E(C):pass
# class F(D,E):pass
# print(A.__mro__)
# print(B.__mro__)
# print(C.__mro__)
# print(D.__mro__)
# print(E.__mro__)
# print(F.__mro__)

# class A:
#     def m1(self):
#         print('A-m1')
# class B(A):
#   def m1(self):
#      print('B-m1')  
# class C(A):
#    def m1(self):
#       print('C-m1')
# class D(B):pass
# def m1(self):
#    print('D-m1')
# class E(C):
#    def m(self):
#       print('E-m1')
# class F(D,E):
#    pass
# f=F()
# f.m1()

      
class Employee:
    def __init__(self,name,age,eid,sal):
        self.name=name
        self.age=age
        self.eid=eid
        self.sal=sal
    def printDetails(self):
        print(f'name is {self.name}')
        print(f'age is {self.age}')
        print(f'eid is {self.eid}')
        print(f'sal is {self.sal}')
class Student:
    def __init__(self,name,age,sid,course,college):
        self.name=name
        self.age=age
        self.sid=sid
        self.course=course
        self.college=college
    def printDetails(self):
        print(f'Name is {self.name}')
        print(f' age is{self.age}')
        print(f'course is {self.course}')
        print(f'college is{self.college}')
class Faculty:
    def __init__(self,name,age,fid,dept,college):
        self.name=name
        self.age=age
        self.fid=fid
        self.dept=dept
        self.college=college
    def printDetails(Self):
        print(f'name is {Self.name}')
        print(f'age is {Self.age}')
        print(f' fid is {Self.fid}')
        print(f' dept is{Self.dept}')
        print(f' college is {Self.college}')

e=Employee('priyanka',24,1024,25000)
e.printDetails()
s=Student('zini',24,102423,'Mtech','xyz college')
s.printDetails()

f=Faculty('dr.chand',558,102325,'cse','abc college')
f.printDetails()

