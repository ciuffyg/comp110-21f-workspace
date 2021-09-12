"""An exercise in remainders and boolean logic."""

__author__ = "730394262"


num: int = int(input("Enter an int: "))
conditiona: int = num % 2
conditionb: int = num % 7

if conditiona + conditionb == 0:
    print("TAR HEELS")
else:
    if num % 2 == 0:
        print("TAR")
    else:
        if num % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")