"""A Basketball Program."""

__author__ = "Gianluca Ciuffreda"


import pandas as pd
from random import randint, uniform
from basket import Player, Team, shoot2, shoot3, madepass, failpass, dunk, layup, stealball, freethrow
from time import sleep

df = pd.read_csv(r"C:\Users\Gianluca Ciuffreda\comp110-21f-workspace\projects\ncaagame\ncaaroster.csv", names=['Team', 'First', 'Last', 'Position', 'OVR', 'PAS', 'DRI', 'FT', '3PT', '2PT', 'JMP', 'DEF'])
team_list: list[str] = ["Alabama", "Arizona", "Arkansas", "Auburn", "Baylor", "Boise St", "Boston College", "Colgate", "Colorado St", "Creighton", "CSU Fullerton", "Davidson", "Delaware", "Duke", "Georgetown", "Georgia St", "Gonzaga", "Houston", "Illinois", "Indiana", "Iowa", "Iowa St", "Kansas", "Kentucky", "Louisville", "Loyola Chicago", "LSU", "Marquette", "Memphis", "Miami", "Michigan", "Michigan St", "Montana", "Murray St", "NC State", "New Mexico St", "Norfolk St", "North Carolina", "Notre Dame", "Ohio St", "Oregon", "Purdue", "Richmond", "S Dakota St", "San Diego St", "San Francisco", "Seton Hall", "St Mary's", "St Peter's", "Syracuse", "TCU", "Tennessee", "Texas", "Texas Tech", "UCLA", "UConn", "USC", "Vermont", "Villanova", "Virginia Tech", "Wichita St", "Wisconsin", "Xavier", "Yale"]
find_roster: dict[str, list[int]] = {}

tick: int = 0
for x in team_list:
    tick2: int = tick + 1
    tick3: int = tick + 2
    tick4: int = tick + 3
    tick5: int = tick + 4
    z: list[int] = [tick, tick2, tick3, tick4, tick5]
    find_roster[x] = z
    tick += 5

team1: str = str(input("Home team:  "))
team2: str = str(input("Away team:  "))

home_team: Team = Team(team1)
away_team: Team = Team(team2)

homescore: int = 0
awayscore: int = 0

possession: Team
ballwith: Player
prevwith: Player
assist: bool = False


def initiate_teams():
    ind1: int = find_roster[team1][0]
    ind2: int = find_roster[team1][1]
    ind3: int = find_roster[team1][2]
    ind4: int = find_roster[team1][3]
    ind5: int = find_roster[team1][4]
    hp1: Player = Player(df["Position"][ind1], df["First"][ind1], df["Last"][ind1], df["OVR"][ind1], df["PAS"][ind1], df["DRI"][ind1], df["FT"][ind1], df["3PT"][ind1], df["2PT"][ind1], df["JMP"][ind1], df["DEF"][ind1])
    hp2: Player = Player(df["Position"][ind2], df["First"][ind2], df["Last"][ind2], df["OVR"][ind2], df["PAS"][ind2], df["DRI"][ind2], df["FT"][ind2], df["3PT"][ind2], df["2PT"][ind2], df["JMP"][ind2], df["DEF"][ind2])
    hp3: Player = Player(df["Position"][ind3], df["First"][ind3], df["Last"][ind3], df["OVR"][ind3], df["PAS"][ind3], df["DRI"][ind3], df["FT"][ind3], df["3PT"][ind3], df["2PT"][ind3], df["JMP"][ind3], df["DEF"][ind3])
    hp4: Player = Player(df["Position"][ind4], df["First"][ind4], df["Last"][ind4], df["OVR"][ind4], df["PAS"][ind4], df["DRI"][ind4], df["FT"][ind4], df["3PT"][ind4], df["2PT"][ind4], df["JMP"][ind4], df["DEF"][ind4])
    hp5: Player = Player(df["Position"][ind5], df["First"][ind5], df["Last"][ind5], df["OVR"][ind5], df["PAS"][ind5], df["DRI"][ind5], df["FT"][ind5], df["3PT"][ind5], df["2PT"][ind5], df["JMP"][ind5], df["DEF"][ind5])
    home_team.pg1 = hp1
    home_team.sg1 = hp2
    home_team.sf1 = hp3
    home_team.pf1 = hp4
    home_team.c1 = hp5

    ind11: int = find_roster[team2][0]
    ind22: int = find_roster[team2][1]
    ind33: int = find_roster[team2][2]
    ind44: int = find_roster[team2][3]
    ind55: int = find_roster[team2][4]
    ap1: Player = Player(df["Position"][ind11], df["First"][ind11], df["Last"][ind11], df["OVR"][ind11], df["PAS"][ind11], df["DRI"][ind11], df["FT"][ind11], df["3PT"][ind11], df["2PT"][ind11], df["JMP"][ind11], df["DEF"][ind11])
    ap2: Player = Player(df["Position"][ind22], df["First"][ind22], df["Last"][ind22], df["OVR"][ind22], df["PAS"][ind22], df["DRI"][ind22], df["FT"][ind22], df["3PT"][ind22], df["2PT"][ind22], df["JMP"][ind22], df["DEF"][ind22])
    ap3: Player = Player(df["Position"][ind33], df["First"][ind33], df["Last"][ind33], df["OVR"][ind33], df["PAS"][ind33], df["DRI"][ind33], df["FT"][ind33], df["3PT"][ind33], df["2PT"][ind33], df["JMP"][ind33], df["DEF"][ind33])
    ap4: Player = Player(df["Position"][ind44], df["First"][ind44], df["Last"][ind44], df["OVR"][ind44], df["PAS"][ind44], df["DRI"][ind44], df["FT"][ind44], df["3PT"][ind44], df["2PT"][ind44], df["JMP"][ind44], df["DEF"][ind44])
    ap5: Player = Player(df["Position"][ind55], df["First"][ind55], df["Last"][ind55], df["OVR"][ind55], df["PAS"][ind55], df["DRI"][ind55], df["FT"][ind55], df["3PT"][ind55], df["2PT"][ind55], df["JMP"][ind55], df["DEF"][ind55])
    away_team.pg1 = ap1
    away_team.sg1 = ap2
    away_team.sf1 = ap3
    away_team.pf1 = ap4
    away_team.c1 = ap5


def passball(bw: Player, b: Player, c: list[Player], d: Team, e: Team):
    global assist, possession, ballwith, prevwith
    who: int = 0
    to: Player = b
    chance1: float = round(uniform(1, 1.5), 1)
    chance2: float = round(uniform(0.5, 1), 1)
    bw.passes += 1
    while who < 1:
        i: int = randint(0, 4)
        if bw == c[i]:
            who += 0            
        else:
            who += 1
            to = c[i]
    if (bw.passing * chance1) > (b.defense * chance2):
        madepass(bw, to)
        prevwith = bw
        bw.passcomplete += 1
        assist = True 
        possession = d
        ballwith = to
    else:
        bw.turnovers += 1
        b.steals += 1
        failpass(bw, b)
        assist = False
        possession = e
        ballwith = b


def rebound(a: Team, b: Team, c: Player, d: Player, e: Player):
    global ballwith, possession
    sleep(1.5)
    chance1: int = randint(1, 3)
    chance2: int = randint(1, 4)
    a_reb: int = c.jump * chance1
    b_reb: int = d.jump * chance2
    e_reb: int = e.jump * chance2
    who: int = randint(1, 4)

    if who == 1:
        if a_reb > b_reb:
            print(f"Rebound {a.name}.")
            c.rebounds += 1
            ballwith = c
            possession = a
        else:
            print(f"Rebound {b.name}.")
            d.rebounds += 1
            ballwith = d
            possession = b
    else:
        if e_reb > a_reb:
            print(f"{b.name} ball.")
            e.rebounds += 1
            ballwith = e
            possession = b
        else:
            print(f"{a.name} ball.")
            c.rebounds += 1
            ballwith = c
            possession = a


def drive(bw: Player, b: Player, d: Team, e: Team) -> int:
    global assist, possession, ballwith
    chance1: float = round(uniform(0.9, 1.5), 1)
    chance2: float = round(uniform(0.5, 1.2), 1)
    choice: int = randint(1, 2)
    drib: int = bw.dribble
    steal: int = b.defense
    drive: float = drib * chance1
    result: int = 0
    sleep(1.5)
    print(f"    {bw.last_name} drives to the basket...")
    sleep(1.5)
    if drive < (steal * chance2):
        bw.turnovers += 1
        b.steals += 1
        possession = e 
        ballwith = b
        stealball(b)
        result = 11
        return result
    elif choice == 1:
        result = dunk(bw, b)
        return result
    else:
        result = layup(bw, b)
        return result


def foul(a: Player, b: Player, d: Team, e: Team) -> int:
    chance2: int = randint(1, 5)
    fchance: int = randint(1, 99) * chance2
    chance1: int = randint(1, 5)
    defense: int = b.defense * chance1

    if defense < fchance:
        sleep(1.5)
        print(f"    {b.last_name} FOULS {a. first_name} {a.last_name}!")
        sleep(1)
        b.fouls += 1
        result = freethrow(a)
        return result
    else:
        r: int = randint(1, 3)
        if r == 1:
            result = shoot2(a, b)
            return result
        elif r == 2:
            result = drive(a, b, d, e)
            return result
        else:
            result = shoot3(a, b)
            return result


def event(a: Player, b: Player, d: Team, e: Team) -> int:
    global pend
    r: int = randint(1, 12)
    result: int = 0
    if r == 1:
        result = shoot2(a, b)
        return result
    elif r == 2:
        result = drive(a, b, d, e)
        return result
    elif r == 3:
        result = shoot3(a, b)
        return result
    elif r == 4 or r == 5:
        result = foul(a, b, d, e)
        return result
    else:
        result = 10
        return result
    

def match(hteam: Team, ateam: Team):
    global ballwith, prevwith, homescore, awayscore, assist, possession
    home: list[Player] = [hteam.pg1, hteam.sg1, hteam.sf1, hteam.pf1, hteam.c1]
    away: list[Player] = [ateam.pg1, ateam.sg1, ateam.sf1, ateam.pf1, ateam.c1]
    
    possession = hteam
    ballwith = hteam.pg1
    prevwith = hteam.c1
    clock_h1: int = 200
    while clock_h1 > 0:
        i: int = randint(0, 4)
        reb1: int = randint(0, 4)
        reb2: int = randint(0, 4)
        player1: Player = home[i]
        player2: Player = away[i]
        if possession == hteam:
            x: int = event(ballwith, player2, hteam, ateam)
            if x == 10:
                passball(ballwith, player2, home, hteam, ateam)
            elif x > 0 and x < 10:
                ballwith.points += x
                homescore += x
                if assist:
                    prevwith.assists += 1
                assist = False
                possession = ateam
                ballwith = player2
                print(f"{hteam.name} - {homescore} | {awayscore} - {ateam.name}\n")
            elif x == 11:
                assist = False
            else:
                rebound(hteam, ateam, home[reb1], away[reb2], away[4])
        else:
            x: int = event(ballwith, player1, ateam, hteam)
            if x == 10:
                passball(ballwith, player1, away, ateam, hteam)
            elif x > 0 and x < 10:
                ballwith.points += x
                awayscore += x
                if assist:
                    prevwith.assists += 1
                assist = False
                possession = hteam
                ballwith = player1
                print(f"{hteam.name} - {homescore} | {awayscore} - {ateam.name}\n")
            elif x == 11:
                assist = False
            else:
                rebound(ateam, hteam, away[reb2], home[reb1], home[4])
        clock_h1 -= 1
        if clock_h1 == 100:
            print(f"\nHaltime.\n{hteam.name}: {homescore}\n{ateam.name}: {awayscore}\n")
            sleep(5)
        
    if homescore == awayscore:
        print(f"\nOvertime!\n{hteam.name}: {homescore}\n{ateam.name}: {awayscore}\n")
        # sleep(5)
        possession = hteam
        clock_o1: int = 60
        while clock_o1 > 0:
            i: int = randint(0, 4)
            reb1: int = randint(0, 4)
            reb2: int = randint(0, 4)
            player1: Player = home[i]
            player2: Player = away[i]
            if possession == hteam:
                x: int = event(ballwith, player2, hteam, ateam)
                if x == 10:
                    passball(ballwith, player2, home, hteam, ateam)
                elif x > 0 and x < 10:
                    ballwith.points += x
                    homescore += x
                    if assist:
                        prevwith.assists += 1
                    assist = False
                    ballwith = player2
                    possession = ateam
                    print(f"{hteam.name} - {homescore} | {awayscore} - {ateam.name}\n")
                elif x == 11:
                    assist = False                
                else:
                    rebound(hteam, ateam, home[reb1], away[reb2], away[4])
            else:
                x: int = event(ballwith, player1, ateam, hteam)
                if x == 10:
                    passball(ballwith, player1, away, ateam, hteam)
                elif x > 0 and x < 10:
                    ballwith.points += x
                    awayscore += x
                    if assist:
                        prevwith.assists += 1
                    assist = False
                    ballwith = player1
                    possession = hteam
                    print(f"{hteam.name} - {homescore} | {awayscore} - {ateam.name}\n")
                elif x == 11:
                    assist = False
                else:
                    rebound(ateam, hteam, away[reb2], home[reb1], home[4])
            clock_o1 -= 1

    print(f"{hteam.read_player_stats()}\n{ateam.read_player_stats()}")
    print(f"\nFinal Score:\n{hteam.name}: {homescore}\n{ateam.name}: {awayscore}")
    # print(f"\n{hteam.read_players()}\n{ateam.read_players()}")
    
    t: int = int(input("Stat report? : "))
    if t > 0:
        hteam.read_stat_rep()
        ateam.read_stat_rep()


def main() -> None:
    initiate_teams()
    match(home_team, away_team)
    print("Thanks for playing.")
    

if __name__ == "__main__":
    main()