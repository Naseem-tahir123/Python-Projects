# Exercise one of three
# Sum of n natural numbers
# ask a user for natural number (n)
# print total from 1 to n


num = int(input("Enter a natural number:"))
total = 0
i = 1
while  i <= num:
    total += i
    i += 1

print(f"the sum of numbers from 1 to {num} is: {total}")