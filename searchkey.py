l=[10,20,30,40,50,80]
i=0
key=int(input('enter the key to search'))
while i<len(l):
    if key==l[i]:
      print(f'{key} is present at {i} index')
    i=i+1
    
# l=[1,4,8,9,90,80,78]
# i=0
# key=int(input('enter the key to search'))
# while i<len(l):
#     if key==