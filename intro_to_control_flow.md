# Intro to control flow


```python
# Control flow

# Like giving python a recipe or an order to do things

# Conditional statements

age = int(input("What is your age?: "))

if age >= 18:
    print("You can watch all movies!")
elif age >= 15:
    print("Sorry you cannot watch 18 rated movies :(, but you can watch all other movies")
elif age >= 12:
    print("Sorry you cannot watch 18 or 15 rated movies :(, but you can watch all other movies")
elif age >= 8:
    print("Sorry you cannot watch 18, 15 or 12 rated movies :(, but you can watch all other movies")
else:
    print("You can only watch U rated movies")

# There are no case or switch statements in Python


```


```python
# For loops and while loops

# for and foreach in other languages
# In python we just user for

list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {
    1: {"name": "Bronson", "money": "$0.05"},
    2: {"name": "Masha", "money": "$3.66"},
    3: {"name": "Roscoe", "money": "$1.14"}
}

for num in list_data:
    print(num * 2)
    
# nested loops

for data in embedded_lists:
    print(data)
    for num in data:
        print(num)

# looping through dictionaries
for item in dict_data.values():
    for embed_value in item.values():
        print(embed_value)
        
# a loop that only returns the money
for items in dict_data.values():
    print(items["money"])

# loops and if statemens
for num in list_data:
    if num == 3:
        print("you have found three!")
    elif num > 3:
        print("gone too far!")
    else:
        print("Too soon!")

# While loops

x = 0

while x < 10:
    print(f"it's working -> {x}")
    x += 1

# While with if statement
while x < 10:
    print(f"it's working -> {x}")
    if x == 4:
        break
    x += 1

# While with if more depth
user_prompt = True

while user_prompt:
    age = input("What is your age?: ")
    if age.isdigit() and int(age) < 117 and int(age) != 0:
        user_prompt = False
    else:
        print("Please enter your age as a digit and under 117")

print(f"Your age is {age} ")
```
 
### Task 1
```python
user_prompt = True

while user_prompt:
     age = input("What is your age?: ")
     if age.isdigit() and 120 > int(age) >= 18:
         print("you can watch any movie!")
         user_prompt = False
     elif age.isdigit() and 120 > int(age) >= 15:
         print("you cannot watch 18 movies but you can watch the rest!")
         user_prompt = False
     elif age.isdigit() and 120 > int(age) >= 12:
         print("you cannot watch 18 or 15 movies but you can watch the rest!")
         user_prompt = False
     elif age.isdigit() and 120 > int(age) <= 11:
         print("you cannot watch 18, 15 or 12 movies but you can watch the rest!")
         user_prompt = False
     else:
         print("Please enter an age between 1 and 120")




```

