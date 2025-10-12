"""
working on some advance min() and max() function
"""

students =  [
    {"name": "Naseem", "score":80, "age":23},
    {"name": "Nadeem", "score":90, "age":20},
    {"name": "Waseem", "score":91, "age":18},

]


# from the above list find the name of studen having higest score

print(max(students , key= lambda item: item.get("score"))["name"])


student2 = {
    "Naseem": { "score":80, "age":23},
    "Nadeem": { "score":90, "age":20},
    "Waseem": { "score":91, "age":18},

}

# from the above dictionary fint the name of student whose age is greatest.

print(max(student2, key = lambda item: student2[item]["age"]))
 