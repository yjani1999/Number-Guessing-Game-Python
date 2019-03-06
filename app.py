print("***** Welcome to the Guessing Game *****")
print("You must guess the number right in 3 tries to win this game")

guess_number = 6
guess_limit = 3
i = 1
is_guess_correct = False
while not is_guess_correct and i <= guess_limit:

    while i <= guess_limit:
        n = int(input("Enter your guess between 0 to 9 :"))
        if n == guess_number:
            print("Wow you guessed it right!!")
            is_guess_correct = True
            break
        else:
            i = i+1
            print("Wrong!")
            is_guess_correct = False
if not is_guess_correct:
    print("Sorry!! You Lost")
elif is_guess_correct:
    print("You Won, Nice Playing with you")

print("***** Developed by Yash Jani *****") 