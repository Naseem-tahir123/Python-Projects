"""
Define a function that takes a numer(n)
which returns the cube of number from 1 to n.
example:
cube_finder(3)
{1:1, 2:8, 3:27}
"""

def cube_finder(n):
    # cube = {}
    # for i in range(1, n+1):
    #     cube = {i:i**3}
    return {i: i**3 for i in range(1, n+1)}


print(cube_finder(4))
