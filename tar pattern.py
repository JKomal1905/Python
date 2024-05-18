from ast import Num
import numbers


# def star(num):
#     print('*'*num)
#     if num==5:
#      return
#     star(num+1)
# star(1)
 
# def star(num):
#     print('*'*num)
#     if num==5:
#        return
#     star(num+1)
# star(1)
# def star(num):
#     print('*'*num)
#     if num==1:
#         return
#     star(num-1)

# star(5)
# def sumofallno(n):
#     if n==1:
#      return n 
#     return n +sumofallno(n-1)
# print(sumofallno(4))    
def sumofallno(n):
    if n==1:
        return n
    return n+sumofallno(n-1)
print(sumofallno(8))