n=int(input("enter a number"))
sum=0
for i in range(1,n):
    if(n%i==0):
        print(i,end=" " )
        sum=sum+i
if(n==sum):
    print("it is a perfect number")
else:
    print("not a perfect number")
    