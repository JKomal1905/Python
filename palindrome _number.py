# n=int(input("enter a number"))
# temp=n
# rev=0
# while(n>0):
#     d=n%10
#     rev=rev*10+d
#     n=n//10
# if(temp==rev):
#     print("number is palindrome")
# else:
#     print("not a palindrome number")
n=int(input("enter a number"))
temp=n
rev=0
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
if(rev==n):
    print("number is palindrome")
else:
    print("number is not palindrome")