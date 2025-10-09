"""
Define a function that takes  num, iterable(tuple, list) containing numbers as args
example:
nums = [1,2,3,4]

input ---->funct to_power(3, *nums)
output----> [1, 8, 27, 64]

if the user did't pass any args then give a user a message
hey you did't pass any args

else return list
Note use list comprehension
"""

nums = [1,2,3,4]
def To_power(a, *args):
    # return [i**a if args else "hey you did't pass any args"  for i in args]
    return [i**a for i in args] if args else "hey you did't pass any args"
 

# print(To_power(3,*nums))
print(To_power(3,*nums))


