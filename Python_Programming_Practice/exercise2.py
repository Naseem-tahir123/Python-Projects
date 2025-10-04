"""
Ask a user to input 3 numbers and you have to print average 
of three numbers using string formating

Try to take all three comma separated inputs  in one line.

"""


num1, num2, num3 = input("Enter the three numbers: ").split(",")

print(num1)
print(num2)
print(num3)


print(f"The average of three numbers are {(int(num1) + int(num2) + int(num3))/3} ")
 
