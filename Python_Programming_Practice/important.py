
"""
write a program which give the largest sequence of consecutive numbers in a list
"""
l = [1,2,3,4,6,7,8,9,10,2,3,4,]

def largest_sequence(l):
    max_len = 0
    current_len = 1
    start_index = 0
    max_start_index = 0
    for i in range(1, len(l)):
        if l[i] == l[i-1] + 1:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
                max_start_index = start_index
            current_len = 1
            start_index = i
    if current_len > max_len:
        max_len = current_len
        max_start_index = start_index
    return l[max_start_index:max_start_index + max_len]
print(largest_sequence(l))
