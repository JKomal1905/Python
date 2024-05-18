# class car:
#     def __init__(self,cname,ccolour,cprice):
#         self.cname=cname
#         self.ccolour=ccolour
#         self.cprice=cprice
#     def printcarDetails(self):
#         print(f' car name is{self.cname}')
#         print(f' car colour is{self.ccolour}')
#         print(f' car price is{self.cprice}')
# class laptop:
#     def __init__(self,lname,lcolour,lprice):
#         self.lname=lname
#         self.lcolour=lcolour
#         self.lprice=lprice
#     def printcarDetails(self):
#         print(f' laptop name is{self.lname}')
#         print(f' laptop colour is{self.lcolour}')
#         print(f' laptop price is{self.lprice}')
# class employee:
#     def __init__(self,ename,eid,eaddress):
#         self.ename=ename 
#         self.eid=eid
#         self.eaddress=eaddress
#         self.c=car('thar','black', 123455677)
#         self.l=laptop('hp','blue',50000)
#     def printDetails(self):
#         print(f'  employee name is {self.ename}')
#         print(f' employee id is {self.eid}')
#         print(f' employee address is {self.eaddress}')
#         self.c.printcarDetails()
#         self.l.printcarDetails()
# e=employee('priyanka','1024','cuttack')
# e.printDetails()
class department:
    def __init__(self,dname,did):
        self.dname=dname
        self.did=did
    def printdepartmentDetails(self):
        print(f' department name is{self.dname}')
        print(f' department id is{self.did}')
class university:
    def __init__(self,uname,uaddress):
        self.uname=uname
        self.uaddress=uaddress
        self.d=department('bsc','101')
    def printuniversityDetails(self):
        print(f' university name is{self.uname}')
        print(f' university address is {self.uaddress}')
        self.d.printdepartmentDetails()
u=university('sbp','sambalpur')
u.printuniversityDetails()
        