"""
write a program that 
filter odd even
define a function which takes a list as an input
and retrun a list containing sublist of odd and even numbers seperately

i.e., [1,2,3,4,5,,6,7,8] ------> [[1,3,5],[2,4,6,8]]

"""

def Even_odd_sublist(lst):
    output = []
    even_list = []
    odd_list = []
    for i in lst:
        if i%2 == 0:
            even_list.append(i)
        elif i%2 != 0:
            odd_list.append(i)
    output = [odd_list , even_list]
    return output

print(Even_odd_sublist([1,2,3,4,5,6,7,8,9,10]))