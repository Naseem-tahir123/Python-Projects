        # program to find greatest number among  three numbers
# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>c and b>a:
#         return b
#     else:
#         return c
# print(greatest(1,2,3))


    # writer a program that takes 3 number from user and print the greatest one:
# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>c and b>a:
#         return b
#     else:
#         return c
# num1 = int(input("enter the first number : "))
# num2 = int(input("enter the second number : "))
# num3 = int(input("enter the third number : "))
# greater  = greatest(num1, num2, num3)
# print(f"the greater number is : {greater}")

def smallest(a,b,c):
    if a<b and a<c:
        return a
    elif b<c and b<a:
        return b
    else:
        return c
num1 = int(input("enter the first number : "))
num2 = int(input("enter the second number : "))
num3 = int(input("enter the third number : "))
small_no= smallest(num1, num2, num3)
print(f"the smallest number is : {small_no}")