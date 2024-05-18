from ctypes import HRESULT
import datetime
#working with date
# d=datetime.date(2022,9,19)
# print(d)
# print(d.month)
# print(d.year)
# print(d.day)
# t=datetime.time(10,23,14,786969)
# print(t)
# print(t.hour)
# print(t.minute)
# print(t.second)
# dt=datetime.datetime(2022,9,19,10,23,50,7123)
# print(dt)
# print(dt.year)
# print(dt.month)
# print(dt.day)
# print(dt.hour)
# print(dt.second)
# current_dt=datetime.datetime.now()
# print(current_dt)
# print(current_dt.year)
# print(current_dt.month)
# print(current_dt.hour)
# wap to wish to the user based on time
# 6-12--->good morning
# 12-18---->good afternoon
# 18-22--->good evening
# 22-6---->good night
# current_dt=datetime.datetime.now()
# hr=current_dt.hour
# #print(current_dt.hour)
# if hr>=6 and hr<12:
#     print("hi good morning")
# elif hr>=12 and hr<18:
#     print("good afternoon")
# # elif hr>=6 and hr<22:
#     print("hello good evening")
# else:
#     print("by good night")
current_dt=datetime.datetime.now()
print(current_dt)
print(current_dt.strftime('%B'))
print(current_dt.strftime('%A'))
print(current_dt.strftime('%D'))
print(current_dt.strftime('%w'))
    