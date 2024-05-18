# wap to search a value from a list then display its index.
# if the value is present multiple times then print its all indices and also count the number of times that value is repeated in the list.
# l=[10,20,30,10,40,50,20,60]
# i=0
# key=int(input("enter the key to search"))
# while i<len(l):
#     if key==l[i]:
#      print(f'{key} is present at {i} index')
#     i=i+1 
# l=[10,20,30,40,50,60,40,30,10]
# i=0
# key=int(input('enter the key to be search'))
# while i<len(l):
#     if key==l[i]:
#         print(f'{key} is present at {i} index')
#     i=i+1 
l=[10,20,30,30,40,20,10]
i=0
key=int(input('enter the key to be searched'))
while i<len(l):
    if key==l[i]:
        print(f'{key} is present at {i} index')
    i=i+1