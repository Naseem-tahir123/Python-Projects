import time
from functools import wraps

def cal_time(func):
    @wraps(func)
    def wrapper_funct(*args, **kwargs):
        print(f"Executing ...... {func.__name__}")
        start = time.time()
        returned = func(*args, **kwargs)
        end = time.time()
        time_taken = end - start
        print(f"total time taken by the function to run {time_taken}")
        return returned
    
    return wrapper_funct

@ cal_time
def sq(l):
    squares = []
    for i in l:
        squares.append(i**2)
    return squares

l1 = list(range(1,51))

print(sq(l1))
 
