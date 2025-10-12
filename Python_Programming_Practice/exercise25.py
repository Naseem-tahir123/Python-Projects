"""
Write a function that take multiple lists as input having equal length,
and gives us the average of list in such a way as below

[1,2,3], [4,5,6], [7,8,9]

(1+4+7)/3, (2+5+8)/3, (3+6+9)/3
"""


def average_finder(*args):
    average = []
    pairs = zip(*args)
    # print(list(pairs))
  
    for pair in pairs:
        average.append(sum(pair)/len(pair))
    return average


print(average_finder([1,2,3], [4,5,6], [7,8,9]))


# Solution by Lambda Function

average_finder1 = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]

print(average_finder1([1,2,3], [4,5,6], [7,8,9]))

