# using for loop
# write a program that take a multidigit number i.e "1345" and sum all the digit as 1+3+4+5. while taking input a number from user don't 
#  change it into interger.
num = input("enter a number : ")
total = 0
for i in range(0,len(num)):
    total+=int(num[i])
print(f"total sum is {total}")