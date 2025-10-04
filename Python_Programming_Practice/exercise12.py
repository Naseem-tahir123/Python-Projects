"""
Write a program which gives the fibbnoci sequence of a number

i.e., 10 ----> 0 1 1 2 3 5 8 13 
"""
num = int(input("Enter a number: "))
a = 0
b = 1

def Fibbanoci(x):
    a = 0 
    b = 1
    if x == 1:
        print(a, end=" ")
    elif x == 2:
        print(a,b, end=" ")
 
    else:
        print(a, b, end=" ") 
        for i in range(1, x-1):
            c = a + b
            print(c, end=" ")
            a = b
            b = c
    

Fibbanoci(num)

 
        


