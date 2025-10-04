"""
Ask a user to enter a number containing more than one digit
example: 2345
calculate: 2+3+4+5 and print


"""

num = input("Enter a number cantaining more than one digit: ")

total = 0 

# for i in num:
#     # j = int(i)
#     # total += j
#     total += int(i)


# print(f"The total is: {total}")



# Now same problem soluting using while loop
i = 0
while i < len(num):
    total += int(num[i])
    i += 1

print(f"The total is: {total}")
