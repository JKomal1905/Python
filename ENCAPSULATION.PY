# class college:
#     def __init__(self):
#         self.__balance=5000
#     def getbalance(self):
#         return self.__balance
# c=college()
# print(c.getbalance())
class college:
    def __init__(self):
        self.__balance=5000
    def getBalance(self,password):
        if password==1005:
         return self.__balance
        else:
           print("invalid user")
c=college()
print(c.getBalance(1005))

