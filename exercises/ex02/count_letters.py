"""Counting letters in a string."""

__author__ = "730394262"


letter: str = str(input("What letter do you want to search for?: "))
word: str = str(input("Enter a word: "))
count: int = 0
i: int = 0

while i < len(word):
    if word[i] == letter:
        count = count + 1
    i = i + 1
    
print("Count: " + str(count))