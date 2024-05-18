#  creation of instance variable inside constructor
# class student:
#     def __init__(self,name,age,roll):
#         self.name=name
#         self.age=age
#         self.roll=roll
# s1=student('priyanka',24,1024)

# print(s1.__dict__)

# creation of instance variable inside instance method
# class student:
#     def create(self,name,age,roll):
#         self.name=name
#         self.age=age
#         self.roll=roll
# s1=student()
# s1.create('rahul',25,1025)
# print(s1.__dict__)
#
# creation of instance variable outside instance method
class student:
    def __init__(self,name):
      self.name=name 
s1=student('zini')
print(s1.__dict__)
s1.age=24
  