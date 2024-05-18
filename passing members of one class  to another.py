class student:
    def __init__(self,name,age,roll,address):
        self.name=name
        self.age=age
        self.roll=roll
        self.address=address
    def printDetails(self):
        print(f'name is {self.name}')   
        print(f'age is {self.age}') 
        print(f'roll is {self.roll}') 
        print(f'address is {self.address}') 
s1=student('priyanka',24,1024,'bbsr')
s1.printDetails()

class normal:
    @staticmethod
    def modify(r):
        r.address='cuttack'
normal.modify(s1)
s1.printDetails()