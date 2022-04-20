
import random 
wining_number = random.randint(1,100)
guess = 1
number = int(input("guess a number between 1 and 100 : "))
game_over =False
while not game_over:
    if number==wining_number:
        print(f"congr you win in {guess} guess time")
        game_over = True
    else:
        if number> wining_number:
            print("too high : ")
            guess+=1
            number = int(input("guess again : "))
        else:
            print("too low : ")
            number = int(input("guess again : "))
            guess+=1


    