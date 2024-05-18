# class A:
#     def __init__(self):
#         self._x=23
# class B(A):
#     def test(self):
#         print(self._x)
# b=B()
# b.test()

# class A:
#     def __init__(self):
#         self.__x=23
#     def test(self):
#         print(self.__x)
# a=A()
# a.test()
 
class A:
    def __init__(self):
        self.__x=23
a=A()
print(a.__x)