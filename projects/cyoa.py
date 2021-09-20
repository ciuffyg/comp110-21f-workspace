"""Create Your Own Adventure: Project 00. WORLD CUP PENALTY SHOOTOUT."""

__author__ = "730394262"


from random import randint
player: str = ""
userteam: str = ""
userflag: str = ""
points: int = 10
# list of countries
c1: str = "Italy"
c2: str = "Germany"
c3: str = "Spain"
c4: str = "USA"
GOAL: str = '\U000026BD'
MISS: str = '\U0000274C'
TROPHY: str = '\U0001F3C6'
SKULL: str = '\U0001F480'
CONFETTI: str = '\U0001F389'


def finalmatch(x: int, y: str, z: str) -> int:
    """Play for it all! This function returns the players points value after they play out the FINAL of the World Cup! Bigger points rewards!"""
    team2: str = "France"
    i: int = 0
    team1score: int = 0
    team2score: int = 0
    team1kicks: int = 0
    team2kicks: int = 0
    print(f"Opponent: {team2}")
    while i < 10:
        if i % 2 == 0:
            print(f"{z} steps up to shoot for {y}... ")
            gkguess2: int = randint(1, 3)
            kick2: int = int(input("Enter an integer to shoot... (1: kick left, 2: shoot middle, 3: kick right): "))
            team1kicks = team1kicks + 1
            if kick2 == gkguess2:
                print(f"-15 {MISS} Saved by the keeper!!! - {y} {team1score} / {team1kicks}")
                x = x - 15
            else:
                if kick2 > 3:
                    x = x - 15
                    print(f"-15 {MISS} Shot was off target!!! - {y} {team1score} / {team1kicks}")
                    print(f"{z} kicked the ball way off target. Make sure you choose an int between 1 and 3 to place your shot accurately.")
                else:
                    if kick2 < 1:
                        x = x - 15
                        print(f"-15 {MISS} Shot was off target!!! - {y} {team1score} / {team1kicks}")
                        print(f"{z} kicked the ball way off target. Make sure you choose an int between 1 and 3 to place your shot accurately.")
                    else:
                        team1score = team1score + 1
                        print(f"+40 {GOAL} {z} scored! - {y} {team1score} / {team1kicks}")
                        x = x + 40
            i = i + 1
            print(f"(Points balance: {x})")
        else:
            print(f"{team2} step up to shoot... ")
            kick3: int = randint(1, 3)
            gkguess3: int = int(input("Enter an integer to save the shot! (1: dive left, 2: dive middle, 3: dive right): "))
            team2kicks = team2kicks + 1
            if kick3 == gkguess3:
                print(f"+40 {MISS} Saved by {player}!!! - {team2} {team2score} / {team2kicks}")
                x = x + 40
            else:
                team2score = team2score + 1
                print(f"-15 {GOAL} Scored! - {team2} {team2score} / {team2kicks}")
                x = x - 15
                if gkguess3 > 3:
                    print(f"{z} was frozen in place and didn't react. Make sure you choose an int between 1 and 3 to save the shot.")
                else:
                    if gkguess3 < 1:
                        print(f"{z} was frozen in place and didn't react. Make sure you choose an int between 1 and 3 to save the shot.")
            i = i + 1
            print(f"(Points balance: {x})")
    if team1score == team2score:
        print(f"{SKULL} SUDDEN DEATH! {SKULL}")
        while team1score == team2score:
            print(f"{z} steps up to shoot for {y}... ")
            gkguess4: int = randint(1, 3)
            kick4: int = int(input("Enter an integer to shoot... (1: kick left, 2: shoot middle, 3: kick right): "))
            team1kicks = team1kicks + 1
            if kick4 == gkguess4:
                print(f"-15 {MISS} Saved by the keeper!!! - {y} {team1score} / {team1kicks}")
                x = x - 15
            else:
                if kick4 > 3:
                    x = x - 15
                    print(f"-15 {MISS} Shot was off target!!! - {y} {team1score} / {team1kicks}")
                    print(f"{z} kicked the ball way off target. Make sure you choose an int between 1 and 3 to place your shot accurately.")
                else:
                    if kick4 < 1:
                        x = x - 15
                        print(f"-15 {MISS} Shot was off target!!! - {y} {team1score} / {team1kicks}")
                        print(f"{z} kicked the ball way off target. Make sure you choose an int between 1 and 3 to place your shot accurately.")
                    else:
                        team1score = team1score + 1
                        print(f"+40 {GOAL} {z} scored! - {y} {team1score} / {team1kicks}")
                        x = x + 40
            i = i + 1
            print(f"(Points balance: {x})")
            print(f"{team2} step up to shoot... ")
            kicka: int = randint(1, 3)
            ugkguessa: int = int(input("Enter an integer to save the shot! (1: dive left, 2: dive middle, 3: dive right): "))
            team2kicks = team2kicks + 1
            if kicka == ugkguessa:
                print(f"+40 {MISS} Saved by {player}!!! - {team2} {team2score} / {team2kicks}")
                x = x + 40
            else:
                team2score = team2score + 1
                print(f"-15 {GOAL} Scored! - {team2} {team2score} / {team2kicks}")
                x = x - 15
                if ugkguessa > 3:
                    print(f"{z} was frozen in place and didn't react. Make sure you choose an int between 1 and 3 to save the shot.")
                else:
                    if ugkguessa < 1:
                        print(f"{z} was frozen in place and didn't react. Make sure you choose an int between 1 and 3 to save the shot.")
            i = i + 1
            print(f"(Points balance: {x})")
    if team1score > team2score:
        x = x + 500
        print(f"{CONFETTI} Congratulations {CONFETTI}, {z}, you won the World Cup! {TROPHY} +500 points!")
    else:
        print(f"Sorry, {z}, you lose.")
    global points
    points = x
    return x


def match() -> None:
    """Standard procedure for an exhibition match."""
    team1: str = userteam
    team2: str = "Brazil"
    i: int = 0
    team1score: int = 0
    team2score: int = 0
    team1kicks: int = 0
    team2kicks: int = 0
    print(f"Opponent: {team2}")
    while i < 10:
        if i % 2 == 0:
            print(f"{player} steps up to shoot for {team1}... ")
            gkguess0: int = randint(1, 3)
            kick0: int = int(input("Enter an integer to shoot... (1: kick left, 2: shoot middle, 3: kick right): "))
            team1kicks = team1kicks + 1
            if kick0 == gkguess0:
                print(f"-10 {MISS} Saved by the keeper!!! - {team1} {team1score} / {team1kicks}")
                global points
                points = points - 10
            else:
                if kick0 > 3:
                    points = points - 10
                    print(f"-10 {MISS} Shot was off target!!! - {team1} {team1score} / {team1kicks}")
                    print(f"{player} kicked the ball way off target. Make sure you choose an int between 1 and 3 to place your shot accurately.")
                else:
                    if kick0 < 1:
                        points = points - 10
                        print(f"-10 {MISS} Shot was off target!!! - {team1} {team1score} / {team1kicks}")
                        print(f"{player} kicked the ball way off target. Make sure you choose an int between 1 and 3 to place your shot accurately.")
                    else:
                        team1score = team1score + 1
                        print(f"+30 {GOAL} {player} scored! - {team1} {team1score} / {team1kicks}")
                        points = points + 30
            i = i + 1
        else:
            print(f"{team2} step up to shoot... ")
            kick1: int = randint(1, 3)
            gkguess1: int = int(input("Enter an integer to save the shot! (1: dive left, 2: dive middle, 3: dive right): "))
            team2kicks = team2kicks + 1
            if kick1 == gkguess1:
                print(f"+30 {MISS} Saved by {player}!!! - {team2} {team2score} / {team2kicks}")
                points = points + 30
            else:
                team2score = team2score + 1
                print(f"-10 {GOAL} Scored! - {team2} {team2score} / {team2kicks}")
                points = points - 10
                if gkguess1 > 3:
                    print(f"{player} was frozen in place and didn't react. Make sure you choose an int between 1 and 3 to save the shot.")
                else:
                    if gkguess1 < 1:
                        print(f"{player} was frozen in place and didn't react. Make sure you choose an int between 1 and 3 to save the shot.")
            i = i + 1

    if team1score == team2score:
        print(f"{SKULL} SUDDEN DEATH! {SKULL}")
        while team1score == team2score:
            print(f"{userteam} step up to shoot... ")
            gkguess: int = randint(1, 3)
            kick: int = int(input("Enter an integer to shoot... (1: kick left, 2: shoot middle, 3: kick right): "))
            team1kicks = team1kicks + 1
            if kick == gkguess:
                print(f"-10 {MISS} Saved by the keeper!!! - {team1} {team1score} / {team1kicks}")
                points = points - 10
            else:
                if kick > 3:
                    print(f"-10 {MISS} Shot was off target!!! - {team1} {team1score} / {team1kicks}")
                    print("Your player kicked the ball way off target. Make sure you choose an int between 1 and 3 to place your shot accurately.")
                    points = points - 10
                else:
                    if kick < 1:
                        print(f"-10 {MISS} Shot was off target!!! - {team1} {team1score} / {team1kicks}")
                        print("Your player kicked the ball way off target. Make sure you choose an int between 1 and 3 to place your shot accurately.")
                        points = points - 10
                    else:
                        team1score = team1score + 1
                        print(f"+30 {GOAL} Scored! - {team1} {team1score} / {team1kicks}")
                        points = points + 30
            print(f"{team2} step up to shoot... ")
            kick: int = randint(1, 3)
            gkguess: int = int(input("Enter an integer to save the shot! (1: dive left, 2: dive middle, 3: dive right): "))
            team2kicks = team2kicks + 1
            if kick == gkguess:
                print(f"+30 {MISS} Saved by {player}!!! - {team2} {team2score} / {team2kicks}")
                points = points + 30
            else:
                team2score = team2score + 1
                print(f"-10 {GOAL} Scored! - {team2} {team2score} / {team2kicks}")
                points = points - 10
                if gkguess > 3:
                    print("Your keeper was frozen in place and didn't react. Make sure you choose an int between 1 and 3 to save the shot.")
                else:
                    if gkguess < 1:
                        print("Your keeper was frozen in place and didn't react. Make sure you choose an int between 1 and 3 to save the shot.")
    if team1score > team2score:
        points = points + 30
        print(f"Congratulations, {player}, you won! +30 points!")
    else:
        print(f"Sorry, {player}, you lose. Points: {points}")


def greet() -> None:
    """Standard greeting procedure."""
    name: str = str(input(f"Welcome to {TROPHY} FIFA WORLD CUP Penalty Shootout! --- Play exibition matches to accumulate points or simulate the world cup final to compete for higher points rewards!\nRULES:\nIn a penalty shootout, two teams get five chances to shoot and score a goal ({GOAL}) while the opponents try to save ({MISS}) it!\nIf the contest is tied after 5 shots each, it goes to {SKULL} sudden death {SKULL}!\nWhat is your name: "))
    i: int = 0
    global player
    player = name
    while i != 1:
        print(f"Select a nation: 1: {c1}, 2: {c2}, 3: {c3}, 4: {c4}. ")
        nationchoice: int = int(input("My nation (enter an int): "))
        if nationchoice == 1:
            global userteam 
            userteam = c1
            i = i + 1
        else:
            if nationchoice == 2:
                userteam = c2
                i = i + 1
            else:
                if nationchoice == 3:
                    userteam = c3
                    i = i + 1
                else:
                    if nationchoice == 4:
                        userteam = c4
                        i = i + 1
                    else:
                        print("Please select a nation from the list. Capitalization matters!")
    print(f"You have selected {userteam}. ")


def main() -> None:
    print(greet())
    i: int = 0
    while i != 1:
        print("Main Menu: \n1. Play an exhibition match\n2. Play the Final!\n3. End Game ")
        stepx: int = int(input("Choose option 1, 2, or 3: "))
        if stepx == 1:
            print(match())
            print(f"Total points: {points}")
        else:
            if stepx == 2:
                print(finalmatch(points, userteam, player))
                print(f"Total points: {points}")
            else:
                if stepx != 3:
                    print("Please select a valid option. ")
                else:
                    i = i + 1
    print(f"Game over... Thank you for playing!\nTotal points earned: {points}")


if __name__ == "__main__":
    main()