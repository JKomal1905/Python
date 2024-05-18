# from threading import*
# print(enumerate())
from threading import*
import time
def fun1():
    time.sleep(3)
    print('i m fun1')
def fun2():
    time.sleep(3)
    print('i m fun2')
t1=Thread(target=fun1)
t1.start()
t2=Thread(target=fun2)
t2.start()
l=enumerate()
for i in l:
    print(i.name)
    print(i.ident)
