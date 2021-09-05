"""Repeating a beat in a loop."""

__author__ = "730394262"


counter: int = 1
beat: str = str(input("What beat do you want to repeat? "))
repmax: int = int(input("How many times do you want to repeat it? "))
beatrep: str = beat

if repmax <= 0:
    print("No beat...")
else:
    while counter < repmax:
        beatrep = beatrep + str(" ") + beat
        counter = counter + 1
    print(beatrep)