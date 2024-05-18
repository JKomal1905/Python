l=[1,2,3,4,5,6]
choice=int(input("enter your lucky number"))
while True:
    if choice in l:
        print("yes present")
else:
   print("not present")
choice=int(input("enter your number again"))
