"""Finding duplicate letters in a word."""

__author__ = "730394262"

word: str = input("Enter a word: ")
i: int = 0
t: int = 0
dupcount: int = 0

while i < len(word):
    while t < len(word):
        if word[i] == word[t]:
            dupcount = dupcount + 1
        t = t + 1
    i = i + 1
    t = 0

if dupcount > len(word):
    print("Found duplicate: True")
else:
    print("Found duplicate: False")
