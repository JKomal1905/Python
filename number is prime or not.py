n=int(input("enter a number"))
temp=0
for i in range(2,n):
    if n%i==0:
        temp=1
        break
if temp== 1: 
 print("not a prime number")
else:
   print("prime number")
