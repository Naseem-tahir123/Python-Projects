# using for loop write a program that takes the name of user as input and counts the number of each alphabet user in the name.print
# for example in name "naseem "
#  n : 1
#  a : 1
#  s : 1 
#  e : 2 
#  m : 1

name = input("Please enter your name : ")
temp = ""
for i in range(0,len(name)):
    if   name[i] not in temp:
        print(f"{name[i]} : {name.count(name[i])}")
        temp += name[i]
