import random

winning_num = random.randint(1, 10)

guess_num = int(input("Guess a number: "))
while guess_num != winning_num:
    print("Wrong number, try again!")
    guess_num = int(input("Guess a number: "))
print("You win!")
