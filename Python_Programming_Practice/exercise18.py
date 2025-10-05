"""
define a function which takes a list which containg sublist 
and in output it should give us the number of sublists in that list

i.e.,
Input: [1,2,3,4,a,f,[5,6],d,e,f, [x,y]]
Output: 2
"""


def SubListCounter(lst):
    count = 0
    for i in lst:
        if type(i) == list:
            count +=1
    return count

print(SubListCounter([1,2,3,4,[5,6],["x","y"], [1,2,4]]))


 