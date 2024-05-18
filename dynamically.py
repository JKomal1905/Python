d={}
while True:
    key=input('enter the key')
    val=input('enter the value')
    d[key]=val
    choice=input('do you want to add more (Y/N):').upper()
    if choice=='N':
        break
    print(d)
