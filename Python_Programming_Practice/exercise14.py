"""
Define a function which will take a list as an argument and 
this function will return a reversed list

example
[1,2,3,4] -----------> [4,3,2,1]
['word1', 'word2'] ---------------> ['word2', 'word1']

note you simply do this with reverse method or [::-1]
But try to do this with the help of append and return method
"""

# lst = list(range(1,11))
def reverse_lst(l):
    reversed_list = []
    for i in range(1,len(l)+1):
        pop_item = l.pop()
        reversed_list.append(pop_item)
    return reversed_list


lst = ['naseem', 'nadeem', 'waseem', 'asim']


print(reverse_lst(lst))

 