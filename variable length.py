# # def fun(a,b,c,d,e):
# #     print(a,b,c,d,e)

# # fun(10,20,30,40,50,60)

# # def fun(*a):
# #     print(a)

# # fun(10,20,30,40,50,60)
# # fun(10)
# # fun()

# variable length keyword argument+positional argument
# def fun(x,*a):
#     print('x is :',x)
#     print('a is:',a)

# fun(10,20,30,40)
# def fun(*a,x):
#     print('x is :',x)
#     print('a is:',a)

# fun(10,20,30,40)
# def fun(*a,x):
#     print('x is :',x)
#     print('a is:',a)

# fun(x=10,20,30,40)
# def fun(*a,x):
#     print('x is :',x)
#     print('a is:',a)

# fun(10,20,30,x=40)

# default argument+variable length argument
 
# def fun(x=10,*a):
#     print('x is :',x)
#     print('a is:',a)

# fun(10,20,30,  x=789)
# def fun (a,b,*n,x=10):
#     print(a)
#     print(b)
#     print(n)
#     print(x)

# fun(10,20,30,40,x=50) 
  
# def fun(**a):
#     print(a)

# fun(x=10,y=20 )

def fun(**a,*b):
    print(a)
fun()