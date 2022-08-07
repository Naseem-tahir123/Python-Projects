# from pickle import FALSE, TRUE


# def str_from_list(l):
#     return[str(i) for i in l if(type(i)==int or type(i)==float)]
# l = [TRUE, FALSE, [1,2,3,4],1,3.3,2,5]
# print (str_from_list(l))
from re import M


# my_list = []
# nums= [1,2,3,4,5,6,7,8,9,10]
# for i in nums:
#     if i%2==0:
#         my_list.append(i*2)
#     else:
#         my_list.append(-i)
# print(my_list)
# my_list2 = [(i*2) if i%2==0 else (-i) for i in nums]
# print(my_list2)
# even = []
# for i in range(1,11):
#     if i%2==0:
#         even.append(i)
# print(even)

new = [ ]
for i in range(4):
    new.append([1,2,3,4])
print(new)

new1 = [[i for i in range(1,5)] for j in range(4)]
print(new1)