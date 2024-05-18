import random
# print(random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9))
otp=''
for i in range(4):
    otp=otp+str(random.randint(0,9))
    print(otp)