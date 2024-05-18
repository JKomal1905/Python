# class calculation:
#      def __init__(self,a,b):
#           self.a=a
#           self.b=b
#      def add(self):
#         result=self.a+self.b
#         print(f'addition is {result}')
# c1=calculation(10,5)
# c1.add()
# c2=calculation(20,4)
# c2.add()

# instance method inside instance method
# class calculation:
#      def __init__(self,a,b):
#           self.a=a
#           self.b=b
#      def add(self):
#         result=self.a+self.b
#         print(f'addition is {result}')
#         self.sub()
#      def sub(self):
#         result=self.a-self.b
#         print(f'subtraction is {result}')
# c1=calculation(10,5)
# c1.add()
# c2=calculation(20,4)
# c2.sub()

# class calculation:
#      def __init__(self,a,b):
#           self.a=a
#           self.b=b
#      def add(self):
#         result=self.a+self.b
#         print(f'addition is {result}')
      
#      def sub(self):
#         result=self.a-self.b
#         print(f'subtraction is {result}')
# c1=calculation(10,5)
# c1.add()
# c2=calculation(20,4)
# c2.sub()

# modify,delete
class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def update(self,m,n):
        self.a=m
        self.b=n
    def delete(self):
        del self.a
t1=Test(10,20)
print(t1.__dict__)
t1.update(88,99)
print(t1.__dict__)



