import random

num = random.randrange(11)
tries = 5

while tries > 0:
    guess = int(input("Guess the number 0-10: "))
    if guess == num:
        print("Correct")
        break
    elif guess > num:
        print("Guess lower.\n")
        tires = tries - 1
    elif guess < num:
        print("Guess higher.\n")
        tries = tries - 1
    else:
        print("Invalid input.\n")
        tries = tries - 1
    


if tries == 0:
    print("Game over.")