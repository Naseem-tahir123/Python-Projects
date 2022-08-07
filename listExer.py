 
def reverseAlphbt(l):
    Element = []
    for i in l:
        Element.append(i[::-1])
    return Element
strings = ['abc','defg','hig']
print(reverseAlphbt(strings))

def odd_even_seprator(l):
    even = []
    odd = []
    for i in l:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    output = [even,odd]
    return output
nums = list(range(1,20))
print(odd_even_seprator(nums))

def common(l,k):
    commn = []
    for i in l:
        if i in k:
            commn.append(i)
 
    return commn
l1 = [1,2,3,4]
l2 = [8,9, 6, 7]
print(common(l1,l2))