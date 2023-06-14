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
    

```