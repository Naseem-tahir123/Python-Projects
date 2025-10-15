"""
Function returning function
it is also called closure or first class function

"""


def outer_funct():
    def inner_funct():
        print("Inside inner function. ")
    return inner_funct


var = outer_funct()
var()

def func1(msg):
    def func2():
        print(f"the message is: {msg}")
    return func2

var1 = func1("Hello brothers")
var1()


"""
Define a function which can calculate power 
"""
def to_pow(pow):
    def cal_pow(num):
        return num**pow
    return cal_pow

square = to_pow(2)
print(square(8))


cube= to_pow(3)
print(cube(2))


