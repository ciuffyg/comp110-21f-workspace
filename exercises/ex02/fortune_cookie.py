"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730394262"

from random import randint

fortune: int = randint(1, 4)

print("Your fortune cookie says... ")

if fortune == 1:
    print("You have a big promotion in your future. Try walking backwards through doors for good luck. ")
else:
    if fortune == 2:
        print("The love of your life will be wearing jeans and an Apple Jack's t-shirt. ")
    else:
        if fortune == 3:
            print("The Wicked Welsh Witch of Watford will haunt you till the end of time. ")
        else:
            if fortune == 4:
                print("You will do better on quiz 01 than on quiz 00. ")

print("Now, go spread positive vibes! ")