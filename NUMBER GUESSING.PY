import random
rn=random.randint(1,10)
while True:
    choice=int(input("guess a number in between 1-10:"))
    if choice==rn:
        print("cong!!! your guess correct number")
    elif choice>rn:
        print("sry!!! your guess is greater than computer generated number")
    else:
        print('sry!!! your guess is less than computer generated number')