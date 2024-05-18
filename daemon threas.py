from threading import*
import time
# print(current_thread().daemon) 
# def fun1():
#     for i in range(5):
#         print(i)
#         time.sleep(1)

# t1=Thread(target=fun1,daemon=True)
# print('t1 thread is daemon:',t1.daemon)
# t1.start()
# time.sleep(2)
# print('end of main thread')

def fun1():
    for i in range(5):
        print('hi')
        time.sleep(1)
    t2=Thread(target=fun2,daemon=False)
    t2.start()
    print('t2 thread is daemon:',t2.daemon)

def fun2():
    for i in range(5):
        print('hello')
        time.sleep(1)
t1=Thread(target=fun1,daemon=True)
print('t1 thread is daemon:',t1.daemon)
t1.start()
time.sleep(10)
print('end of main thread')