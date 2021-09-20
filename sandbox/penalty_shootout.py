"""World Cup Penalty Shootout Game."""

__author__ = "730394262"

from random import randint

GOAL: str = '\U000026BD'
MISS: str = '\U0000274C'
team1: str = input("Home team: ")
team2: str = input("Away team: ")
i: int = 0
team1score: int = 0
team2score: int = 0
t1k: int = 0
t2k: int = 0

while i < 10:
    if i % 2 == 0:
        print("-----")
        print(str(team2) + " step up... ")
        kick: int = randint(1, 3)
        gkguess: int = int(input("Guess: "))
        if kick == gkguess:
            print(MISS + " Saved by the keeper!!!")
        else:
            team2score = team2score + 1
            print(GOAL + " Scored!")
        t1k = t1k + 1
        i = i + 1
        print(str(team2) + " " + str(team2score) + "/" + str(t1k))
    else:
        print("-----")
        print(str(team1) + " step up... ")
        kick: int = randint(1, 3)
        gkguess: int = int(input("Guess: "))
        if kick == gkguess:
            print(MISS + " Saved by the keeper!!!")
        else:
            team1score = team1score + 1
            print(GOAL + " Scored!")
        t2k = t2k + 1
        i = i + 1
        print(str(team1) + " " + str(team1score) + "/" + str(t2k))

if team1score == team2score:
    while team1score == team2score:
        print("-----")
        print("Sudden Death! ")
        print(str(team2) + " step up... ")
        kick: int = randint(1, 3)
        gkguess: int = int(input("Guess: "))
        if kick == gkguess:
            print(MISS + " Saved by the keeper!!!")
        else:
            team2score = team2score + 1
            print(GOAL + " Scored!")
        t1k = t1k + 1
        i = i + 1
        print(str(team2) + " " + str(team2score) + "/" + str(t1k))
        print("-----")
        print(str(team1) + " step up... ")
        kick: int = randint(1, 3)
        gkguess: int = int(input("Guess: "))
        if kick == gkguess:
            print(MISS + " Saved by the keeper!!!")
        else:
            team1score = team1score + 1
            print(GOAL + " Scored!")
        t2k = t2k + 1
        i = i + 1
        print(str(team1) + " " + str(team1score) + "/" + str(t2k))

print("-----")
print("Final Score: " + str(team2) + " " + str(team2score) + " --- " + str(team1score) + " " + str(team1))