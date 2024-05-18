# from threading import *
# def fun1():
#             for i in range(2):
#              print('rahul')
# def fun2():
#             for i in range(2):
#              print('priyanka')
                     
# fun1()
# fun2()
# t1=Thread(target=fun1)
# t1.start()
# t2=Thread(target=fun2)
# t2.start()
#
# from threading import *
# print('line-23:',current_thread().name )
# def fun1():
#       print('line-18:',current_thread().name )
#       for i in range(2):
#                print('rahul')
# def fun2():
#          print('line-18:',current_thread().name )
#          for i in range(2):
#              print('priyanka')
                     
# fun1()
# fun2()
# t1=Thread(target=fun1)
# t1.start()
# t2=Thread(target=fun2)
# t2.start()
# print('line-27:',current_thread().name )
# t1=Thread(target=fun1)
# print('line-22:',current_thread().name )
# t1.start()
# print('line-36:',current_thread().name )
# t2.start()
# print('line-23:',current_thread().name )
# print('line-20:',active_count() )
# ''''''


# from threading import *
# def fun1():
#       for i in range(2):
#                print('rahul')
# def fun2():
#          for i in range(2):
#              print('priyanka')
                    
# t1=Thread(target=fun1)
# t1.start()
# print('line-51:',active_count())
# t2=Thread(target=fun2)
# t2.start()
# print('line-48:',active_count())

# from threading import *
# def fun1():
#     for i in range(5):
#         print('i',i)
# def fun2():
#     for j in range(5):
#         print('j',j)
# t1=Thread(target=fun1)
# t1.start()

# fun1()
from threading import *
print('line 70:',current_thread().name)
def fun1():
    print('line 72:',current_thread().name)
    for i in range(5):
        print('i',i)
def fun2():
    print('line 73:',current_thread().name)
    for j in range(5):
        print('j',j)
t1=Thread(target=fun1)
t1.start()
print('line 75:',current_thread().name)
fun1()


    