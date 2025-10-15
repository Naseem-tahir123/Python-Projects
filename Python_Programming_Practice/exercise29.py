"""
Function as an argument
"""
def square(a):
    return a**2
l = [1,2,3,4]
print(list(map(square, l)))



def my_map(funct, l):  # where funct is a function and l is any iterable (i.e., list)
    """ take a function and an iterable as input, apply the the function to the iterable and returns the output"""
    new_list = []
    for i in l:
        new_list.append(funct(i))
    return new_list

print(my_map(lambda x: x**3, l))
print(my_map.__doc__)

print(len.__doc__)
print (my_map.__name__)
