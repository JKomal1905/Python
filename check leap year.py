year=int(input("enter a year"))
if(year%4==0):
    print("it is a leap year")
elif(year%400==0)&(year%100!=0):
    print("it is a leap year")
else:
    print("not a leap year")