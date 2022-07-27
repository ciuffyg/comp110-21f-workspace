"""A Basketball Program."""

__author__ = "Gianluca Ciuffreda"


import pandas as pd
from random import uniform, randint


class Player:
    """Defines a player and their attributes."""
    first_name: str
    last_name: str
    pos: str
    age: int
    team: str

    play: float
    mpg: float

    three_r: float
    ft_r: float
    orb_p: float
    drb_p: float
    ast_p: float
    stl_p: float
    blk_p: float
    tov_p: float
    usg_p: float
    three_p: float
    two_p: float
    ft_p: float
    
    def __init__(self, a: str, b: str, c: str, age: int, d: str, play: float, mpg: float, e: float, f: float, g: float, h: float, i: float, j: float, k: float, ll: float, m: float, n: float, o: float, p: float):
        self.first_name = a
        self.last_name = b
        self.pos = c
        self.age = age
        self.team = d
        self.play = play
        self.mpg = mpg
        self.three_r = e
        self.ft_r = f
        self.orb_p = g
        self.drb_p = h
        self.ast_p = i
        self.stl_p = j
        self.blk_p = k
        self.tov_p = ll
        self.usg_p = m
        self.three_p = n
        self.two_p = o
        self.ft_p = p
    
    def __repr__(self) -> str:
        return (f'{self.first_name} {self.last_name}')

    def read(self):
        print(f"{self.first_name} {self.last_name} ({self.age}) {self.team} {self.pos}\n    {self.play}\n")


df = pd.read_csv(
    r"C:\Users\Gianluca Ciuffreda\comp110-21f-workspace\projects\nbastats.csv", 
    names=['First', 'Last', 'Pos', 'Age', 'Team', 'Play', 'MPG', '3PAr', 'FTr', 'ORB%', 'DRB%', 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', '3P%', '2P%', 'FT%'], 
)


home_roster: list[Player] = []
away_roster: list[Player] = []
a_oncourt: list[Player] = []
b_oncourt: list[Player] = []

possession: list[Player]
home_score: int = 0
away_score: int = 0
playclock: int = 0
clock: int = 2880


def initiate() -> None:
    global a_oncourt, b_oncourt
    tm1: str = str(input("Home Team:  "))
    tm2: str = str(input("Away Team:  "))
    i: int = 0
    while i < 605:
        p: Player = Player(
            df["First"][i],   # type: ignore
            df["Last"][i],  # type: ignore
            df["Pos"][i],  # type: ignore
            df["Age"][i],  # type: ignore
            df["Team"][i],  # type: ignore
            df["Play"][i],  # type: ignore
            df["MPG"][i],  # type: ignore
            df["3PAr"][i],  # type: ignore
            df["FTr"][i],  # type: ignore
            df["ORB%"][i],  # type: ignore
            df["DRB%"][i],  # type: ignore
            df["AST%"][i],  # type: ignore
            df["STL%"][i],  # type: ignore
            df["BLK%"][i],  # type: ignore
            df["TOV%"][i],  # type: ignore
            df["USG%"][i],  # type: ignore
            df["3P%"][i],  # type: ignore
            df["2P%"][i],  # type: ignore
            df["FT%"][i],  # type: ignore
        )
        if p.team == tm1:
            home_roster.append(p)
        elif p.team == tm2:
            away_roster.append(p)
        i += 1
    a_oncourt = sub_court(home_roster)
    b_oncourt = sub_court(away_roster)
    print("initiated teams.")


def sub_court(a: list[Player]) -> list[Player]:
    a_index: dict[Player, list[float]] = {}
    step: float = 0.000
    result: list[Player] = []
    max_: float = 0.000
    count: int = 5
    i: int = 0
    while i < len(a):
        x: float = step
        y: float = a[i].play + step
        a_index[a[i]] = [x, y]
        if y > max_:
            max_ = y
        i += 1
        step = y
    while count > 0:
        r: float = uniform(0.000, max_)
        for key in a_index:
            if r > a_index[key][0] and r <= a_index[key][1]:
                who: Player = key
                dup: int = 0
                i2: int = 0
                while i2 < len(result):
                    if who == result[i2]:
                        dup += 1
                    i2 += 1
                if dup == 0:
                    result.append(who)
                    count -= 1
    # print("subbed in players.")
    return result


def change(a: list[Player], b: list[Player], c: list[Player]) -> str:
    if a != b:
        global possession
        possession = b
        return (f"{b[0].team} ball.")
    else:
        possession = c
        return (f"{c[0].team} ball.")


def rebound(a: list[Player], b: list[Player]):
    global possession, clock, playclock
    a_index: dict[Player, list[float]] = {}
    b_index: dict[Player, list[float]] = {}
    offe: list[Player]
    defe: list[Player]
    step: float = 0.000
    max_: float = 0.000
    i: int = 0
    if possession == home_roster:
        offe = home_roster
        defe = away_roster
        while i < len(a):
            y: float = a[i].orb_p + step
            a_index[a[i]] = [step, y]
            if y > max_:
                max_ = y
            i += 1
            step = y
        i = 0
        while i < len(b):
            y: float = b[i].drb_p + step
            b_index[b[i]] = [step, y]
            if y > max_:
                max_ = y
            i += 1
            step = y
    else:
        defe = home_roster
        offe = away_roster
        while i < len(a):
            y: float = a[i].drb_p + step
            a_index[a[i]] = [step, y]
            if y > max_:
                max_ = y
            i += 1
            step = y
        i = 0
        while i < len(b):
            y: float = b[i].orb_p + step
            b_index[b[i]] = [step, y]
            if y > max_:
                max_ = y
            i += 1
            step = y
    who: float = uniform(0.000, max_)
    for key in a_index:
        if who > a_index[key][0] and who <= a_index[key][1]:
            # print(f"{a_index[key]} got the rebound.")
            playclock += randint(0, 24 - playclock)
            possession = offe
    for key in b_index:
        if who > b_index[key][0] and who <= b_index[key][1]:
            # print(f"{b_index[key]} got the rebound.")
            possession = defe
            clock -= playclock
            

def shot(a: Player, b: Player) -> int:
    global clock, playclock
    t: float = uniform(0.000, 1.000)
    pt: int = 0
    playclock += randint(0, 16 - playclock)
    if t <= a.three_r:
        hit: float = uniform(0.000, 1.000)
        if hit <= a.three_p:
            pt += 3
            clock -= playclock
        else:
            rebound(a_oncourt, b_oncourt) 
    else:
        block: float = uniform(0.000, 1.000)
        if block <= b.blk_p:
            # print("shot blocked.")
            clock -= playclock
        else:
            hit: float = uniform(0.000, 1.000)
            if hit <= a.two_p:
                pt += 2
                clock -= playclock
            else:
                rebound(a_oncourt, b_oncourt)
    return pt
    

def whogotit(a: list[Player]) -> Player:
    a_index: dict[Player, list[float]] = {}
    step: float = 0.000
    result: Player = a[0]
    max_: float = 0.000
    i: int = 0
    while i < len(a):
        x: float = step
        y: float = a[i].usg_p + step
        a_index[a[i]] = [x, y]
        if y > max_:
            max_ = y
        i += 1
        step = y
    r: float = uniform(0.000, max_)
    for key in a_index:
        if r > a_index[key][0] and r <= a_index[key][1]:
            result = key
            return result


def whoondefense(a: list[Player]) -> Player:
    max_: int = len(a)
    i: int = randint(0, max_ - 1)
    result: Player = a[i]
    return result


def play(a: Player, b: Player):
    global possession, home_score, away_score, clock, playclock, a_oncourt, b_oncourt, home_roster, away_roster
    r: float = uniform(0.000, 100.000)
    playclock += randint(1, 8)
    if r >= 0 and r <= b.stl_p:
        # print(f"{b.first_name} {b.last_name} stole the ball.")
        change(possession, home_roster, away_roster)
        clock -= playclock
    elif r > b.stl_p and r <= (b.stl_p + a.tov_p):
        # print("turnover.")
        change(possession, home_roster, away_roster)
        clock -= playclock
    else:
        if possession == home_roster:
            home_score += shot(a, b)
            possession = away_roster
        else:
            away_score += shot(a, b)
            possession = home_roster
    playclock = 0
    a_oncourt = sub_court(home_roster)
    b_oncourt = sub_court(away_roster)
    # print("a play happened.")


def match(a: list[Player]) -> None:
    global clock, possession
    possession = a 
    while clock > 0:
        ballwith: Player
        defender: Player
        if possession == a:
            ballwith = whogotit(a_oncourt)
            defender = whoondefense(b_oncourt)
        else:
            ballwith = whogotit(b_oncourt)
            defender = whoondefense(a_oncourt)
        play(ballwith, defender)
    print(home_score)
    print(away_score)


def main() -> None:
    initiate()
    match(home_roster)


if __name__ == "__main__":
    main()