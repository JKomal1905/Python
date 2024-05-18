# class A:
#     def method1(self):
#      self.x=10
#      self.y=20
#      print(self.x is {self.x} )
#      print(self.y )
#     def method2(self):
#        self.k=200
#        self.l=100
#        print(self.k)
#        print(self.l)
# class B(A):
#        pass 
# b=B()
# b.method1()
# b.method2()
   
# class A:
#     def im(self):
#         print('parent class instance method')
#     @classmethod
#     def cm(cls):
#         print('parent class method')
#     @staticmethod
#     def sm():
#         print('parent class static method')
# class B(A):
#         pass
# b=B()
# b.im()
# b.cm()
# b.sm()

class A:
    def im(self):
        print('parent class instance method')
        self.i=10

class B(A):
        pass
a=A()
a.im()

