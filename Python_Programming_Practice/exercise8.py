"""
Ask a user for name
Example: Naseem Tahir
print count of each word
output:
N : 1
a : 2
s : 1
e : 2
m : 1
  : 1
T : 1
h : 1
i : 1
r : 1

"""

name = input("Enter your name: ")

temp_val = ''
i = 0

while i  < len(name):
    if name[i] not in temp_val:
        temp_val += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1



