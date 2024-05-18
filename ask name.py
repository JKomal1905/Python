import time
from threading import *

# def sec_count():
#     sec=0
#     while True:
#         time.sleep(5)
#         sec=sec+5
#         print(f'i m waiting since {sec} sec')
# t1=Thread(target=sec_count,daemon=False)
# t1.start()
# name=input('enter your name:\n')
        

        #tradition approach
#isdaemon()

# print("Main Thread is daemon:",current_thread().isDaemon())

#SET DAEMON
# def fun1():
#     for i in range(5):
#      print('hi')
#     time.sleep(1)
# t1=Thread(target=fun1)
# t1.setDaemon(True)
# t1.start()
#once a thread started  we can not change its nature
def fun1():
    for i in range(5):
        print('hello')
        time.sleep(1)
t1=Thread(target=fun1)
t1.start()
t1.daemon=True