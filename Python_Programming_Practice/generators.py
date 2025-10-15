"""
Generators
A generator is a special type of iterator that allows you to iterate over a sequence
of values without storing them all in memory at once.

Benifits of Generators:
1. Memory Efficiency: Generators generate values on-the-fly, which means 
they use less memory compared to lists or other data structures that store all values in memory.
2. Lazy Evaluation: Generators produce values only when requested,
which can lead to improved performance, especially when dealing with large datasets or infinite sequences.
3. Simplicity: Generators can simplify code by eliminating the need for maintaining
 state or managing complex data structures.
4. Infinite Sequences: Generators can represent infinite sequences,
    allowing you to work with potentially unbounded data without running out of memory.

    
"""


l = [1, 2, 3, 4, 5 ]



# working behind the loop
# l = iter(l)
# print(next(l))  # 1
# print(next(l))  # 2
# print(next(l))  # 3
# print(next(l))  # 4




num = map(lambda x: x**2, l)
for i in num:
    print(i)
 

"""
 Create first generator function
"""

def my_gen(n):
    for i in range(1, n+1):
        yield i



# agar kisi sequence ko ik dafa istemal karna ho to generator use kartay hain
nums = my_gen(10)
for i in nums:
    print(i)


for i in nums:
    print(i)