# write a program that take input age of user and print the following result:
# if age  is less than or equal to 10, then ticket for those is free,
# if age is greater than 10 and less than or equal to 15 , then tickek price for those is 50 rupees'
# if age is greater than 15 and less than or equla to 60, then ticket price for those people is 150 rupees,
# and if the age is greater than 60, then ticket for those is also free.
age = float(input("enter your age : "))
if age<=0 or age>100:
    print("sorry you are unable to buy ticket")
elif 0<age<=10:
    print("charge for your ticket is free :")
elif 10<age<=15:
    print("please pay 100 rupees for your ticket")
elif 15<age<=60:
    print("please pay 150 rupees for your ticket")
else:
    print("no charges for your ticket")
 