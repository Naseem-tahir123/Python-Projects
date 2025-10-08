"""
Define a function that takes list of strings 
and in output gives us list containing reverse of every string

Note: Use list comprehension because we already did this exercise 
using normal method

example l = ['abc','def','ghi']
        l_rev = ['cba', 'fed', 'ihg']
"""


def Reverse_lst(lst):
    # return [i[::-1] for i in lst]
    rev_lst = []
    for i in lst:

        rev_lst.append(i[::-1])
    return rev_lst


print(f"Through normal method: {Reverse_lst(['abc','def','ghi'])}")


# Now by list comprehension

def Rev_lst(lst):
    return [i[::-1] for i in lst]


print(f"By using list comprehension: {Rev_lst(['abc','def','ghi'])}")



