# class outer:
#     def __init__(self):
#         print('outerclass constructor')
#     class inner():
#      def __init__(self): 
#         print('inner class constructor')

#outer  class object creation
# o=outer()
# i=inner()
# inner class object creation
# i=o.inner()
# i1=outer.inner()
# i2=outer().inner()
    
# inner with inner
class outer:
    def __init__(self):
        print('outerclass constructor')
    class inner():
     def __init__(self): 
        print('inner class constructor')
    class inner1():
     def __init__(self):
        print('inner1 class constructor')
    class Innerinner():
     def __init__(self):
        print('Innerinner class constructor')
o=outer()
i=o.inner()
i1=o.inner1()
ii=outer.Innerinner()
obj=o.Innerinner()
           