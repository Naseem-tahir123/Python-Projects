from functools import wraps

def only_datatype_allow(datatype):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if all([type(arg) == datatype for arg in args]):
                return func(*args, **kwargs)
            print("Invalid argument! ")
        return wrapper
    return decorator


@only_datatype_allow(str)
def join_str(*args):
    str1 = ''
    for i in args:
        str1 += i + " "
    return str1


print(join_str("Naseem", "Tahir", 23))

    