a=int(input('enter first value'))
b=int(input('enter second value'))
choice=input('enter choice\n add\n sub\n mul\n div\n')
if choice=='add':
    print(a+b)
elif choice=='sub':
        print(a-b)
elif choice=='mul':
        print(a*b)
elif choice=='div':
        print(a/b)
else:
       print('invalid option')