"""
any() and all() function in python
"""

l1 = [2,4,6,8]
l2 = [1,3,5,7]
l3 = [1,2,3,4]

# 1) Check whether the all element of l1 is even or not if yes return True in output

# Through normal method
def all_even(l):
    for i in l:
        return i%2 == 0
    
print(all_even(l1))
        
# Through list comprehension

print(all([i%2==0 for i in l1]))


# 2) Check whether the all element of list is odd or not if yes return True in output if not return False

# Through normal method

def all_odd(l):
    for i in l:
        return i%2 !=0
print(all_odd(l2))

# Through list comprehension

print(all([i%2 !=0 for i in l2]))

"""
3) Now Check whether the single element of list is even or not if yes return True in output 
if not return False

"""

print(any([i%2 == 0 for i in l3]))

"""
3) Now Check whether the single element of list is odd or not if yes return True in output 
if not return False

"""
print(any([i%2!=0 for i in l1]))


"""
When to use any() and all()  function below is the best use case
"""

def add(*args):
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        total = 0
        for num in args:
            total +=num
        return total
    else:
        return "Wrong Input"
    
x = [1,2,3,4,5,7.0,9.0]
y = [1,2,3,"a", ["naseem","waseem"]]

print(add(*x))
print(add(*y))












