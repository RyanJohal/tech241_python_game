# Fizz Buzz

# user_number = int(input("Enter number: "))
#
# if user_number % 2 == 0:
#     print("The number is even!")
# else:
#     print("The number is odd")

# for loop
for num in range(1, 50):
    if num % 5 == 0 and num % 3 == 0:
        print("Fizz Buzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)

# while loop
num = 1
while num < 100:
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)
    num +=1