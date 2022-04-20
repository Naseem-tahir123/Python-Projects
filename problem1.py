# write a program that takes the name of user as input and print the count of each lsalphabet





name = input("enter your name : ")
i=0
double_val = ""
while i<len(name):
    if name[i] not in double_val:
        double_val = double_val + name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i+=1