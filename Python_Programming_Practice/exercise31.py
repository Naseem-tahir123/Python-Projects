"""
Decorator:
is a function that enhances the functionality of other function
"""

def decorator_funct(funct):
    def wrapper_func():
        print("This method is very helpful")
        funct()
    return wrapper_func
@ decorator_funct
def func1():
    print("The name of function is func1")
@ decorator_funct
def func2():
    print("The name of function is func2")

# func1 = decorator_funct(func1)
# func1()

# func2 = decorator_funct(func2)
# func2()

  

print("\n\n")

func1()
