# find sum of all elements present inside list without using lambda
# from functools import reduce
# def addall(x,y):
#     return x+y
# l=[1,2,3,4,5]
# data=reduce(addall,l)
# print(data)
#  with using lambda
# from functools import reduce
# l1=[1,2,3,4,5,6]
# data=reduce(lambda x,y:x+y,l1)
# print(data)

# from functools import reduce
# l=[1,2,3,45,6]
# data=print(reduce(lambda x,y:x*y,l))

# find out sum of all the numbers from 1-100

# from functools import reduce
# data=reduce(lambda x,y:x+y,range(1,101))
# print(data)

# from functools import reduce
# names=['surendra','priyanka','rahul','zini']
# data=print(reduce(lambda x,y:x+y,names))

# from functools import reduce
# l=[1,2,3,4,5,6]
# data=print(reduce(lambda x,y:x+y,l,100))
# print(type(data))

# from itertools import accumulate
# l=[1,2,3,4,5,6]
# data =print(list(accumulate(l,lambda x,y:x+y)))
