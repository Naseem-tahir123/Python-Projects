"""
write a common element finder function
which takes 2 list as input and return a list
which contains common elements of both lists

example

input [1,2,3,4], [1,2,5,6,7]
output [1,2]
"""

def CommonElementFinder(lst1,lst2):
    output = []
    for i in lst1:
        if i in lst2:
            output.append(i)
    return output

print(CommonElementFinder([1,2,3,4],[1,2,5,6,3]))