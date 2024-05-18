# d={}
# while True:
#     key=input('enter the key')
#     val=input('enter the value')
#     d[key]=val
#     choice=input('do you want to add more element[Y/N]')
#     if choice=='NO':
#       break
# print(d)

d={}
while True:
    key=input('enter the key')
    val=input('enter the value')
    d[key]=val
    choice=input('do you want to add more element [Y/N]')
    if choice=='N':
        break
    print(d)
