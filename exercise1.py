# num1 =input("enter first number : ")
# num2 = input ("enter second number : ")
# num3 = input ("enter third number : ")
num1,num2,num3 = input("enter three number separate by comma ").split(",")
num4 = (int(num1)+int(num2)+int(num3))/3
print(f"average is {num4}")