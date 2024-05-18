# class calculation:
#     @staticmethod
#     def add(a,b):
#         print(f' addition is {a+b}')
#     @staticmethod
#     def sub(a,b):
#         print(f' subtraction is{a-b}')
# calculation.add(10,20) 
# c1=calculation()
# c1.add(100,200)

# inside a class using class name
class calculation:
    @staticmethod
    def add(a,b):
        print(f' addition is {a+b}')
        calculation.sub(20,10)
    @staticmethod
    def sub(a,b):
        print(f' subtraction is{a-b}')
calculation.add(10,20) 
c1=calculation()
c1.add(100,200)