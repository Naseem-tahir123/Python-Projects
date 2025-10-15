"""
Advance sorted functions
"""

fruits = ["mango","apple","grapes"]
fruits.sort()
print(fruits)


fruits2 = ("mango","apple","grapes")
print(sorted(fruits2))


fruits3 = {"mango","apple","grapes"}
print(sorted(fruits3))


bikes = [
    {"model":"honda", "price":150000},
    {"model":"hero", "price":100000},
    {"model":"road prince", "price":90000}


]

print(sorted(bikes, key = lambda bikes: bikes["price"], reverse=True), )


 