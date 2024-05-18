# def outer():
#     print('hello outer')

#     def inner():
#         print('hello inner')
#     print('-----------')
#     return inner
# # outer()

def outer():
    print('hello outer')

    def inner():
        print('hello inner')
    print('-----------')
    return inner
x=outer()
x()     