"""
write  a function which takes two number as input and return 
the number which is greater.
"""

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

def greater_num(a,b):
    if a > b:
        return a
    return b

print(greater_num(num1,num2))
