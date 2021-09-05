"""Example of looping through all characters in a string."""

__author__ = "730394262"

user_string: str = input("Give me a string! ")

# The variable i is a common counter variable name in programming. i is short for iteration or iterator.
i: int = 0

while i < len(user_string):
    print(user_string[i])
    i = i + 1

print("Done! ")
