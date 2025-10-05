"""
Define a function that takes list of words as arguments and 
return list with reverse of every element in that list

example
['abc','def','ghi'] ---------> ['cba', 'fed', 'ihg']
"""

def Reverse(lst):
    reverse_list = []
    for word in lst:
        reverse_list.append(word[::-1])
    return f"The Reversed list is: {reverse_list}"
            # print(i, end=" ")
            

 


print(Reverse(['abc','def','ghi'] ))
 