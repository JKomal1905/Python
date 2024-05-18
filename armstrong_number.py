# n=int(input("enter a number"))
# sum=0
# temp=n
# while (temp>0):
#     digit=temp%10;
#     # cube=digit*digit*digit
#     sum=sum+digit**3
#     temp=temp//10
# if (n==sum):
#     print(" number is armstrong")
# else:
#     print("number is not an armstrong")
n=int(input("enter a number"))
sum=0
temp=n
while (temp>0):
    digit=temp%10;
    cube=digit*digit*digit
    sum=sum+cube
    temp=temp//10
if (n==sum):
    print(" number is armstrong")
else:
    print("number is not an armstrong")