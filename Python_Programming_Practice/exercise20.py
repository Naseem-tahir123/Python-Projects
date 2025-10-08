"""
Take the inputs from user and store into a dictionary

example:
user_detail = {
    "name" : "Naseem",
    "age" : 23,
    "fav_fruits" : ["apple", "banana", "mango"],
    "fav_color" : ["red", "yellow" , "green"]

}
"""

name = input("Enter your name: ")
age = int(input("Enter your age: "))
fav_fruits = input("Enter the name of your favorite fruits: ").split(",")
fav_colors = input("Enter the name of your favorite colors: ").split(",")

# user_details = dict(name,age,fav_fruits,fav_colors)
user_details = {"name":name,"age": age, "fav_fruits" : fav_fruits,"fav_colors":fav_colors}
print(user_details)
for i in user_details:
    print(user_details[i])
