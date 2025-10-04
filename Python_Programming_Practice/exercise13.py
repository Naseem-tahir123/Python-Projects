"""
Define a function which takes list containing numbers as input
and return list containing square of every elements

example
numbers = [1,2,3,4]
square_list(numbers) --------> [1,4,9,16]
"""

lst = [1,2,3,4]

def square_list(l):
    new_lst  = []
    for i in l:
        new_lst.append(i**2)
    return new_lst

print(square_list(lst))