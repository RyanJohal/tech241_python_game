# # Control flow
#
# # Like giving python a recipe or an order to do things
#
# # Conditional statements
#
# age = int(input("What is your age?: "))
#
# if age >= 18:
#     print("You can watch all movies!")
# elif age >= 15:
#     print("Sorry you cannot watch 18 rated movies :(, but you can watch all other movies")
# elif age >= 12:
#     print("Sorry you cannot watch 18 or 15 rated movies :(, but you can watch all other movies")
# elif age >= 8:
#     print("Sorry you cannot watch 18, 15 or 12 rated movies :(, but you can watch all other movies")
# else:
#     print("You can only watch U rated movies")
#
# # There are no case or switch statements in Python

# Weather warnings

temperature = int(input("What is the temperature today?: "))

if temperature >= 30:
    print("Make sure to drink lots of water and do not spend too long in the sun!")
elif temperature >= 18:
    print("Beautiful day outside make sure to enjoy it!")
elif temperature >= 7:
    print("Remember to take a jumper")
elif temperature >= 1:
    print("It's a bit chilly, remember your jaket!")
elif temperature >= -5:
    print("It's freezing, wrap up warm!")
else:
    print("Stay inside")
