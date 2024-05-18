# outside of the class
# class student:
#       college="xyz college"
# print(student.college)
# student.college="abc college"
# print(student.college)

# class student:
#       college="abc college"
#       def __init__(self):
#         college="def college"       
# print(student.college) 
# s1=student
# print(s1.__dict__)
# print(student.__dict__)

# class student:
#     college="ijk college"
#     def modify(self):
#         student.college="lmn college"
#         print(student.__dict__)
# s1=student()
# s1.modify()
# # print(student.__dict__)

# inside class method
# class student:
#     college="opq college"
#     @classmethod
#     def cm(cls):
#         cls.college="stv college"
# print(student.college)
# s1=student()
# s1.cm()
# print(student.college)
# class student:
#     college="opq college"
#     @staticmethod
#     def sm():
#         student.college="stv college"
# print(student.college)
# s1=student()
# s1.sm()
# print(student.college)

# class student:
#     college="opq college"
# s1=student()
# print(student.college)
# s1.college='abc college'
# print(student.college)
# print(s1.__dict__)

# class student:
#     college='xyz college'
#     def __init__(self):
#         self.college='abc college'
# print(student.college)
# s1=student()
# print(student.college)
# print(s1.__dict__)


