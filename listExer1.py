# def list_counter(l):
#     count = 0
#     for i in l:
#         if type(i) == list:
#             count += 1
#     return count
# lis = [1,2,3,[4,5],[34,32]]
# print(list_counter(lis))
#         #python program to find maximum value in an array
 


# array = []
# num = int(input("enter the values : "))
# for i in range(0,num):
#         numbers = int(input())
#         array.append(numbers)
# print(array)
# min_array = array[0]
# for i in range(0,len(array)):
#     if (array[i]<min_array):
#         min_array = array[i]
# print(f"smallest element in array is : {min_array}")

# Write a function which take array as input and print the 
#        average of an array
# def average(n):
#     sumOfNum = 0
#     for i in n:
#         sumOfNum = sumOfNum+i
#     ave = sumOfNum/len(n)
#     return ave
# arr = []
# num = int(input("enter the numbers: "))
# for n in range(0,num):
#     element = int(input())
#     arr.append(element)
# print(arr)

# print(f"Average of arry is {average(arr)}")
 
# write a function which returns sum of two numbers
# def sum(a,b):
#         total = a+b
#         return total
# num1 = int(input("enter the first number"))
# num2 = int(input("enter the secont number"))
# print(sum(num1,num2))
# name = [1,3,4,5]
# # name.append(6)
# # print(name)
# # name.pop()
# print(name.pop())
# print(name)
marks = []
while True:
        num = (input("enter the marks"))
        if num == "n":
                break
        else:
                marks.append(num)
print(marks)
# def abs_func(n):
#         if n<0:
#                 return n*-1
#         return n*1
# num = -20
# print(abs(num))