# Exercise, Number Guessing Game
# Make a variable like winning_number and assign any number to it.
# Ask user to guess a number
# if user correctly the print "You Win !!"
# if user did't guess correctly then:
#     if user guessed number is less than winning_number then print "too low"
#     if user guessed number is greater than winning_number then print "too high"
# google how to generate random number in pyton to "generate random winning number"

import random 
winning_num = random.randrange(1,5)
guess_num = int(input("Enter a random number: "))
if guess_num == winning_num:
    print("YOU Win !!")
elif guess_num < winning_num:
    print("Too low")
else:
    print("Too High")

print(winning_num)