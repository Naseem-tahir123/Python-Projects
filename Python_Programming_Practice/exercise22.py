"""
Write a program that takes   a list as input
and the list can contain any type of items like string, integer, float, list etc
In output we want a list which contain the only the str form of integers.

example: 
input l = ["naseem", "a", [1,2,3], 4,5,6, 1.0, True, False]
output lst = ["4", "5", "6", "1.0" ]
"""


def lst_output(lst):
    output = []
    for i in lst:
        if type(i) == int or type(i) == float:
            output.append(str(i))
    return output

print(f"Using normal method: {lst_output(["naseem", "a", [1,2,3], 4,5,6, 1.0, True, False])}")




def lst_output1(lst):
    return [str(i) for i in lst if (type(i) == int or type(i) == float)]

print(f"Using list comprehension: {lst_output1(["naseem", "a", [1,2,3], 4,5,6, 1.0, True, False])}")

