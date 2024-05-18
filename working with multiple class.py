class student:
    def __init__(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll
    def printDetails(self):
        print('student information')
        print(f' name is {self.name}')
        print(f' age is {self.age}')
        print(f' roll is {self.roll}')
        print('-'*20)
class faculty:
    def __init__(self,name,age,fid):
        self.name=name
        self.age=age
        self.fid=fid
    def printDetails(self):
        print('faculty information')
        print(f' name is {self.name}')
        print(f' age is {self.age}')
        print(f' fid is {self.fid}')
s1=student('priyanka',24,1024)
s1.printDetails()
f1=student('rahul',60,104)
f1.printDetails()

