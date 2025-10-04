# take two comma seperated input from user
# 1. user name --- example "Naseem"
# 2. a single character -- exapmple "e"


# output 2 print lines:

# 1. user name length
# 2. count the character that user inputed (bonus: case insensitive count) 


user_name , character = input("Enter the user name and single character: ").split(",")

# print("Length of user name: " , len(user_name))
# print("Character is: ", character)

# count = 0

# for i in user_name:

#     if i == character:
#         count +=1

# print(f"{character} count : {count}")



# ------------------------- Second Method ---------------------

print(f"Length of user name: {len(user_name.replace(" ",""))}")
print(f"count of {character} in  {user_name} is : {user_name.lower().count(character.replace(" ","").lower())}")
 
    




