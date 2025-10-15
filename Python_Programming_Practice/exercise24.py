"""
Define a function that takes a list of names as input
and in output it returns a list of names with reverse string and the 
first letter capitalized.

i.enput: ["alice", "bob", "charlie"]
o.output: ["Ecila", "Bob", "Eilrahc"]
"""


def reverse_and_capitalize(names):
    output = []
    for name in names:
        output.append(name[::-1].capitalize())
    return output


print(reverse_and_capitalize(["alice", "bob", "charlie"]))
