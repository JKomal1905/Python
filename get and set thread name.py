# from threading import *
# def fun1():
#     print(current_thread().name)
#     for i in range(5):
#         print('surendra')
# def fun2():
#     for i in range(5):
#         print('priyanka')
# t1=Thread(target=fun1)
# t1.start()
# print(t1.name)
# t2=Thread(target=fun2)
# t2.start()
# print(current_thread().name)

# from threading import *
# def fun1():
#     print(current_thread().name)
#     for i in range(5):
#         print('surendra')
# def fun2():
#     for i in range(5):
#         print('priyanka')
# t1=Thread(target=fun1,name='my thread1')
# t1.start()
# print(t1.name)
# t2=Thread(target=fun2 ,name='my thread2')
# t2.start()
# print(current_thread().name)

# from threading import *
# def fun1():
#     print(current_thread().name)
#     for i in range(5):
#         print('surendra')
# def fun2():
#     for i in range(5):
#         print('priyanka')
# t1=Thread(target=fun1)
# t1.name='mythread1' 
# t1.start()
# t2=Thread(target=fun2)
# t2.name='mythread2'
# t2.start()
# print(current_thread().name)
# print(f'old style,t1.getName()')

# import time
# for i in range(5):
#     print(i)
#     time.sleep(5)

# print('surendra')
# time.sleep(2)
# print('rahul')
# time.sleep(2)
# print('priyanka')

# import time
# from threading import *
# def fun1():
#     time.sleep(2)
#     print('surendra')
# def fun2():
#     print('priyanka')
# t1=Thread(target=fun1)
# t2=Thread(target=fun2)

# print('before starting t1 thread',t1.is_alive())
# print('before starting t2 thread',t2.is_alive())

# t1.start()
# t2.start()
# print('after starting t1 thread',t1.is_alive())
# print('after starting t2 thread',t2.is_alive())
import time
from threading import*
def fun1():
    time.sleep(3)

    print('stop-fun1')
def fun2():
    time.sleep(3)  
    print('stop-fun2')
t1=Thread(target=fun1)
t2=Thread(target=fun2)
time.sleep(3)
print('no.of active thread:',active_count())
t1.start()
t2.start()
    






