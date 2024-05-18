class bank:
    bankname="indian express bank"
    branch="a23,BBSR,INDIA"
    # create account
    def __init__(self,username,pan,address):
        self.username=username
        self.pan=pan
        self.address=address
        self.balance=0.0
        print(f'hello{self.username}cong!your account created successfully ')
        # deposit
    def deposit(self, amount):
        self.balance=self.balance+amount
        print(f'{amount} deposited sucessfully')
username=input('enter your name:') 
pan=input('enter pan card number')
address=input('enter your address:')       
b=bank(username,pan,address)
while True:
    print('please select any option:')
    print('n1.deposit\n2.withdrawal\n3.ministatement\n4.stop')
    option=int(input(''))
    if option==1:
        amount=float(input('enter deposited amount:'))
        b.deposit(amount)
    if option==4:
        print('thanks for using indian express bank')
        break

