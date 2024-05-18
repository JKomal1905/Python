# def createlist(r1,r2):
#     if r1==r2:
#         return(r1)
#     else:
#         res=[]
#         while(r1<r2+1):
#             res.append(r1)
#             r1=r1+1
#             return res
#         r1,r2=-1,1
#         print(createlist(r1,r2))
# Python3 Program to Create list
# with integers within given range

# def createList(r1, r2):

# # Testing if range r1 and r2
# # are equal
# if(r1 == r2):
#  return  r1

# else:

# Create empty list
#  res = []

# # loop to append successors to
# # list until r2 is reached.
# while( r1 < r2+1 ):
	
#  res.append(r1)
# r1 += 1
# return res

# # Driver Code
# r1, r2 = -1, 1
# print(createList(r1, r2))


 
# def createlist(r1,r2):
#     return [item for item in range(r1,r2+1)]
# r1,r2=1,11
# print(createlist(r1,r2))

        
# import itertools
# r1=1
# r2=10
# number=list(itertools.chain(range(r1,r2+1)))
# print(number)

# Python3 Program to Create list 
# with integers within given range 
# import numpy as np
# def createlist(r1,r2):
#     return np.arange(r1,r2+1,1)
# r1,r2=1,10
# print(createlist(r1,r2))

# import numpy as np
# def createlist(r1,r2):
#     return np.arange(r1,r2+1,1)
# r1=1
# r2=10
# print(createlist(r1,r2))

# create list  using map lambda function
# 
# def createlist(r1,r2):
#     return list(map(lambda x:x ,range(r1,r2+1)))
# print(createlist(1,10))
# print(createlist(1,-1))

    


