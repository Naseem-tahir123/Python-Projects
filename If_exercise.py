wining_no = 30 # To asssign value to variable we use only single equal sign
gues_no = int(input("enter your guess number : "))
if gues_no==wining_no: # to check equality we use double equal 
    print("Congratulations you win !!!")
else:#  this conditio is also called Nested if else 
    if gues_no >wining_no:
        print("No. you enter is too high")
    else:
        print("No. yoiu enter is too low")