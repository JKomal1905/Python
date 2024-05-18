phy=int(input('enter the mark of phy'))
chem=int(input('enter the mark of chem'))
bio=int(input('enter the mark of bio'))
math=int(input('enter the mark of bio'))
eng=int(input('enter the mark of eng'))
IT=int(input('enter the mark of IT'))

totalmark=phy+chem+bio+math+eng+IT
avgmark=totalmark/6

if avgmark>=90:
    print('O grade')
elif avgmark>=80 and avgmark<=89:
    print('E grade')
elif avgmark>=70 and avgmark<=79:
    print('A grade')
elif avgmark>=60 and avgmark<=69:
    print('B grade')
elif avgmark>=50 and avgmark<=59:
    print('C grade')
elif avgmark>=40 and avgmark<=49:
    print('D grade')
else:
    ('better luck next')