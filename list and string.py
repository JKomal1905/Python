# l=[10,20,'surendra','priyanka',38.5,39,77.9,90.9]
# print(int(l))


# 2
# l=[10,20,30,40,[50,60,70],80,[90,200,205]]
# # print 60 and 200
# # print(l[4][1])
# print(l[6][1])
# #3
# input [10,20,30] and expecyted output is 777,888,999
# l=[10,20,30]
# l[0]=777
# l[1]=888
# l[2]=999
# print(l)
##4
# input one word and print in reverse order
# l=["k","o","m","a","l"]
# print(l)
# l.reverse()
# print(l)
# 5
# input your city name and count number of alphabet k in the name
# city=["tokyo","London","Newyork"]
# for k in city:
#     c=city.count(k)
#     print(c)

# 6enter an alphabet and check that is vowel ar consonent

# vowel=["a","e","i","o","u","A","E","I","O","U"]
# alpha=input("char:")
# if alpha in vowel:
#     print("its is a vowel")
# else:
#     print("it is  consonant")    
# 7
# input 2 nested list and add the elements
# l1=[[10,20,30],[40,50,60],[70,80,90]]
# l2=[[11,12,13],[14,15,16],[17,18,19]]
# l3=[l1[0][0]+l2[0][0],l1[0][1]+l2[0][1],l1[0][2]+l2[0][2]],[l1[1][0]+l2[1][0],l1[1][1]+l2[1][1],l1[1][2]+l2[1][2]],[l1[2][0]+l2[2][0],l1[2][1]+l2[2][1],l1[2][2]+l2[2][2]]
# print(l3)
# 8
# print total  no. of list
# r in surendra
# r in priyanka
# r in rahul

# l2=['rahul']
# l3=['priyanka']
l=['surendra']
for r in l:
 c=l.count(r)
print(c)
# for r in l2:
#     c1=l.count(r)
#     print(c1)
# for r in l3:
#     c2=l.count(r)
#     print(c2)
 


# 11 find 78 is present or not
# l=[10,2,58,67,78,8,7,21]
# for i in l:
#     if i==78:
#         print("78 is present")
#     else:
#         ("not present")
# 12
# l=["kajal"]
# for k in l:
#     c=l.count(k)
#     print(c)

# 13 remove duplicate element
# l=[10,20,20,30,40,40,50,50,50,60,70]
# l.remove(20)
# l.remove(40)
# l.remove(50)
# l.remove(50)
# print(l)
# 3remove all the element except middle one
# l=[10,20,20,40,50,40,60,80,60]
# l1=l[4]
# print(l1)
# del(l)
##swap two numbers
# l=[10,20,30,40,50,60,70,80]
# temp=0
# temp=l[0]
# l[0]=l[7]
# l[7]=temp
# print(l)

##find missing number 
# print all the numbers which is multiply by 3 or divide by 4

# l=[1,2,3,4,6,7,8,9,11,12,13,15,16]
# for i in l:
#     if(i%4==0 and i*3):

#         print(i)
        # i=i+1

# find max number without using max()
# l=[10,20,30,40,50,60,70,80]
# # print(max)
# min=l[0]
# for i in l:
#     if i>min:
#         min=i
#         i=i+1
#     print(i)
# find out minimum value
# l=[10,20,30,40,50,60,70,80] 
# min=l[0]
# for i in l:
#     if i<min:
#         min=i
# print("min is",min)