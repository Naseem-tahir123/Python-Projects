# the code below will print the number from 0 to 4 and break at number 5
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# the code below will print the number from 1 to 10 except 5
for i in range(1, 11):
    if i ==5:
        continue
    print(i)