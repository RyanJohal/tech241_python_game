# Dice game
import random
# Intro screen
while True: # ensures valid input is provided to start game
    start = input("Are you ready to play? (yes/no): ")
    if start == "yes": # checks value of variable
        print("Great, lets play!")
        name = input("What is your name? ")
        print("Welcome " + name)
        break
    elif start == "no":
        print("you scared?")
    else:
        print("Invalid, please enter 'yes' or 'no'")

from random import randint #import libraries

user_score = 0
cpu_score = 0

#Start game
while user_score < 30 and cpu_score < 30: # ensures game continues whilst score is less than 30
    roll = input("Roll dice? (yes/no): ")
    if roll == "yes":
        user_roll = randint(1, 6)
        print(f"You rolled {user_roll}")

        cpu_roll = randint(1, 6)
        print(f"CPU rolled {cpu_roll}")

        user_score += user_roll
        cpu_score += cpu_roll

        print(f"Your new score is {user_score}")
        print(f"CPU new score is {cpu_score}")
    elif roll == "no":
        print("Thanks for playing!")
        break
    else:
        print("Invalid, please enter 'yes' or 'no'")

# End screen
if user_score >= 30 and cpu_score < 30:
    print("Congratulations you win!!!!")
elif user_score >= 30 and cpu_score >= 30:
    print("You tied, good game!")
else:
    print("YOU LOSE, GAME OVER!")
