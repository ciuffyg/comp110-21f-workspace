"""A Basketball Program."""

__author__ = "Gianluca Ciuffreda"


from random import randint, uniform
from time import sleep

BALL: str = "\U0001F3C0"
MISS: str = "\U0000274C"
FIRE: str = "\U0001F525"
CASH: str = "\U0001F4B5"
CHECK: str = "\U00002705"
firstname: list[str] = ["John", "Brady", "Caleb", "Leroy", "DeAndre", "Demar", "Luka", "Armando", "George", "RJ", "Jalen", "DJ", "Derrick", "Erik", "Daniel", "Tom", "Michael", "Russell", "Chris", "Kevin", "Dwayne", "Kyrie", "Damian", "Karl", "Carmelo", "Steve", "Jack", "Alejandro", "Bill", "Hubert", "Mike", "Steph", "Jalen", "Miles", "Devin", "TJ", "AJ", "CJ", "Bud", "Giovanni", "Stefano", "Marco", "Jeremy", "Yao", "Mohamed", "Ibrahim", "Ahmed", "Cho", "Juan", "Carlos", "Luis", "Brook", "Kemba", "Tyler", "Ty", "Al", "Anthony", "Burton", "Cameron", "Cory", "Clark", "Hugo", "Cole", "Reggie", "Grayson", "DeMarcus", "Bruno", "Denis", "Mario", "Ben", "Shawn", "Raymond", "Frank", "Rechon", "Malik", "Jake", "Mo", "Dwight", "Draymond", "Aaron", "Trevor", "Charlie", "Gary", "Jimmy"]
lastname: list[str] = ["Jefferson", "Brady", "Brown", "Smith", "Williams", "DeRozan", "James", "Bacot", "Jordan", "Davis", "Lee", "Murray", "Allen", "Anthony", "Paul", "Irving", "Doncic", "Wade", "Jones", "Curry", "Johnson", "Durant", "Nash", "Thomas", "Ball", "Pierce", "Black", "White", "Villanueva", "Walton", "McCoy", "MacIntosh", "Austin", "Young", "Bridges", "Silva", "Morris", "Morrison", "Santos", "Romano", "Russo", "Bianco", "Lin", "Ming", "Ali", "Adebayo", "Mensah", "Chen", "Garcia", "Lopez", "Gonzalez", "Sanchez", "Adams", "Robinson", "Walker", "Harris", "Guster", "Lewis", "Payne", "Knight", "Green", "Jenkins", "Carter", "Miller", "Bush", "Cousins", "Jokic", "Morant", "Wilkins", "Chamberlain", "Love", "Jin", "Cosby", "Howard", "Gardner", "Fox", "Ward", "Hart", "Butler"]
colleges: list[str] = ["Gonzaga", "Georgia St", "Boise St", "Memphis", "Uconn", "New Mexico St", "Arkansas", "Vermont", "Alabama", "Notre Dame", "Texas Tech", "Montana St", "Michigan St", "Davidson", "Duke", "CSU Fullerton", "Baylor", "Norfolk St", "North Carolina", "Marquette", "Saint Mary's", "Indiana", "UCLA", "Texas", "Virginia Tech", "Purdue", "Yale", "Murray St", "San Francisco", "Kentucky", "Saint Peter's", "Arizona", "Wichita St", "Seton Hall", "TCU", "Houston", "Oregon", "Illinois", "Xavier", "Colorado St", "Michigan", "Tennessee", "Syracuse", "Ohio State", "Loyola Chicago", "Villanova", "Delaware", "Kansas", "NC State", "San Diego St", "Creighton", "Iowa", "Richmond", "Providence", "S Dakota St", "LSU", "Iowa St", "Wisconsin", "Colgate", "USC", "Miami", "Auburn", "Louisville", "Boston College"]

emoji: list[str] = [BALL, FIRE, CASH, CHECK]


class Player:
    """Defines a player and their attributes."""
    first_name: str 
    last_name: str
    position: str
    rating: float

    passing: int
    dribble: int
    free: int
    three: int
    two: int
    jump: int
    defense: int

    shots: int
    made: int
    points: int
    rebounds: int
    blocks: int
    fouls: int
    passes: int
    passcomplete: int
    assists: int
    steals: int
    turnovers: int

    def __init__(self, position: str, first_name: str, last_name: str, rating: float, passing: int, dribble: int, free: int, three: int, two: int, jump: int, defense: int):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.passing = passing + 50
        self.dribble = dribble + 50
        self.free = free + 50
        self.three = three + 50
        self.two = two + 50
        self.jump = jump + 50
        self.defense = defense + 50
        self.rating = rating
        self.shots = 0
        self.made = 0
        self.points = 0
        self.rebounds = 0
        self.blocks = 0
        self.fouls = 0
        self.passes = 0
        self.passcomplete = 0
        self.assists = 0
        self.steals = 0
        self.turnovers = 0

    def readme(self):
        print(f"{self.first_name}\n{self.last_name}\n{self.position}\n{self.rating}\n{self.passing}\n{self.dribble}\n{self.free}\n{self.three}\n{self.two}\n{self.jump}\n{self.defense}")

    def read(self):
        print(f"{self.first_name} {self.last_name} ({self.position})")
        print(f"    Overall: {self.rating} \n")
        print(f"    Passing: {self.passing}")
        print(f"    Dribbling: {self.dribble}")
        print(f"    Free Throw: {self.free}")
        print(f"    Three Point: {self.three}")
        print(f"    Two Point: {self.two}")
        print(f"    Jump: {self.jump}")
        print(f"    Defense: {self.defense} \n")
    
    def read_stats(self):
        print(f"{self.first_name} {self.last_name} ({self.position}) | Pts: {self.points} | Avg: {self.made}/{self.shots} | Ast: {self.assists} | Pas: {self.passcomplete}/{self.passes} | Reb: {self.rebounds} | Bls: {self.blocks} | Stl: {self.steals} | TO: {self.turnovers} | Fl: {self.fouls}")

    def stat_rep(self):
        print(f"{self.first_name}\n{self.last_name}\n{self.position}\n{self.points}\n{self.made}\n{self.shots}\n{self.passcomplete}\n{self.passes}\n{self.assists}\n{self.rebounds}\n{self.steals}\n{self.turnovers}\n{self.blocks}\n{self.fouls}")

    def overall(self):
        """Function to calculate the overall rating of each player by position."""
        if self.position == "PG":
            o: float = round(((self.free * .1) + (self.passing * .2) + (self.dribble * 0.1) + (self.two * .25) + (self.three * .25) + (self.jump * .05) + (self.defense * .05)))
            self.rating = o
        elif self.position == "SG":
            o: float = round(((self.free * .1) + (self.passing * .1) + (self.dribble * 0.1) + (self.two * .3) + (self.three * .3) + (self.jump * .05) + (self.defense * .05)))
            self.rating = o
        elif self.position == "SF":
            o: float = round(((self.free * .1) + (self.passing * .2) + (self.dribble * 0.1) + (self.two * .25) + (self.three * .25) + (self.jump * .05) + (self.defense * .05)))
            self.rating = o
        elif self.position == "PF":
            o: float = round(((self.free * .1) + (self.passing * .15) + (self.dribble * .1) + (self.two * .25) + (self.three * .2) + (self.jump * .1) + (self.defense * .1)))
            self.rating = o
        elif self.position == "C":
            o: float = round(((self.free * .1) + (self.passing * .1) + (self.dribble * 0.1) + (self.two * .3) + (self.three * .05) + (self.jump * .2) + (self.defense * .15)))
            self.rating = o

    def clearstats(self):
        self.shots = 0
        self.made = 0
        self.points = 0
        self.rebounds = 0
        self.blocks = 0
        self.fouls = 0
        self.passes = 0
        self.passcomplete = 0
        self.assists = 0
        self.steals = 0
        self.turnovers = 0


def make_PG() -> Player:
    p: str = "PG"
    a: str = firstname[randint(0, 83)]
    b: str = lastname[randint(0, 78)]

    floor: int = randint(1, 34)
    ceiling: int = floor + 15

    i: float = 0.0
    c: int = randint(floor, ceiling)
    d: int = randint(floor, ceiling)
    e: int = randint(floor, ceiling)
    f: int = randint(floor, ceiling)
    g: int = randint(floor, ceiling)
    h: int = randint(floor, ceiling)
    j: int = randint(floor, ceiling)

    end: Player = Player(p, a, b, i, c, j, d, e, f, g, h)
    end.overall()
    return end


def make_SG() -> Player:
    p: str = "SG"
    a: str = firstname[randint(0, 83)]
    b: str = lastname[randint(0, 78)]

    floor: int = randint(1, 34)
    ceiling: int = floor + 15

    i: float = 0.0
    c: int = randint(floor, ceiling)
    d: int = randint(floor, ceiling)
    e: int = randint(floor, ceiling)
    f: int = randint(floor, ceiling)
    g: int = randint(floor, ceiling)
    h: int = randint(floor, ceiling)
    j: int = randint(floor, ceiling)

    end: Player = Player(p, a, b, i, c, j, d, e, f, g, h)
    end.overall()
    return end


def make_SF() -> Player:
    p: str = "SF"
    a: str = firstname[randint(0, 83)]
    b: str = lastname[randint(0, 78)]

    floor: int = randint(1, 34)
    ceiling: int = floor + 15

    i: float = 0.0
    c: int = randint(floor, ceiling)
    d: int = randint(floor, ceiling)
    e: int = randint(floor, ceiling)
    f: int = randint(floor, ceiling)
    g: int = randint(floor, ceiling)
    h: int = randint(floor, ceiling)
    j: int = randint(floor, ceiling)

    end: Player = Player(p, a, b, i, c, j, d, e, f, g, h)
    end.overall()
    return end


def make_PF() -> Player:
    p: str = "PF"
    a: str = firstname[randint(0, 83)]
    b: str = lastname[randint(0, 78)]

    floor: int = randint(1, 34)
    ceiling: int = floor + 15

    i: float = 0.0
    c: int = randint(floor, ceiling)
    d: int = randint(floor, ceiling)
    e: int = randint(floor, ceiling)
    f: int = randint(floor, ceiling)
    g: int = randint(floor, ceiling)
    h: int = randint(floor, ceiling)
    j: int = randint(floor, ceiling)

    end: Player = Player(p, a, b, i, c, j, d, e, f, g, h)
    end.overall()
    return end


def make_C() -> Player:
    p: str = "C"
    a: str = firstname[randint(0, 83)]
    b: str = lastname[randint(0, 78)]

    floor: int = randint(1, 34)
    ceiling: int = floor + 15

    i: float = 0.0
    c: int = randint(floor, ceiling)
    d: int = randint(floor, ceiling)
    e: int = randint(floor, ceiling)
    f: int = randint(floor, ceiling)
    g: int = randint(floor, ceiling)
    h: int = randint(floor, ceiling)
    j: int = randint(floor, ceiling)

    end: Player = Player(p, a, b, i, c, j, d, e, f, g, h)
    end.overall()
    return end


class Team:
    """Defines a team."""
    name: str
    rating: float
    pg1: Player
    sg1: Player
    sf1: Player
    pf1: Player 
    c1: Player
    
    def __init__(self, name: str):
        self.name = name

    def overall(self):
        result: float = (self.pg1.rating + self.c1.rating + self.pf1.rating + self.sg1.rating + self.sf1.rating) / 5
        self.rating = result
    
    def draft(self):
        pg1: Player = make_PG()
        sg1: Player = make_SG()
        sf1: Player = make_SF()
        pf1: Player = make_PF()
        c1: Player = make_C()
        self.pg1 = pg1
        self.sg1 = sg1
        self.sf1 = sf1
        self.pf1 = pf1
        self.c1 = c1

    def read(self):
        self.overall()
        print(self.name)
        print(f"Overall: {self.rating} \nRoster: \n\n(PG) {self.pg1.first_name} {self.pg1.last_name} ({self.pg1.rating})\n(SG) {self.sg1.first_name} {self.sg1.last_name} ({self.sg1.rating})\n(SF) {self.sf1.first_name} {self.sf1.last_name} ({self.sf1.rating})\n(PF) {self.pf1.first_name} {self.pf1.last_name} ({self.pf1.rating})\n(C) {self.c1.first_name} {self.c1.last_name} ({self.c1.rating})\n")
    
    def readroster(self):
        self.pg1.readme()
        self.sg1.readme()
        self.sf1.readme()
        self.pf1.readme()
        self.c1.readme()

    def read_short(self):
        self.overall()
        print(f"{self.name}: {self.rating}")
    
    def read_players(self):
        print(f"{self.pg1.read()}\n{self.sg1.read()}\n{self.sf1.read()}\n{self.pf1.read()}\n{self.c1.read()}")

    def read_player_stats(self):
        print(f"{self.pg1.read_stats()}\n{self.sg1.read_stats()}\n{self.sf1.read_stats()}\n{self.pf1.read_stats()}\n{self.c1.read_stats()}")
    
    def read_stat_rep(self):
        print(f"{self.pg1.stat_rep()}\n{self.sg1.stat_rep()}\n{self.sf1.stat_rep()}\n{self.pf1.stat_rep()}\n{self.c1.stat_rep()}")

    def __repr__(self) -> str:
        return self.name


ncaa_teams: list[Team] = []


def build_team():
    for x in colleges:
        t: Team = Team(x)
        ncaa_teams.append(t)
        t.draft()


def stealball(a: Player):
    i: int = randint(1, 3)
    if i == 1:
        print(f"{a.last_name} with the steal!")
    elif i == 2:
        print(f"{a.last_name} steals the ball!")
    else:
        print(f"{a.last_name} strips the ball away!")


def made2(a: Player):
    i: int = randint(1, 3)
    j: int = randint(0, 3)
    sleep(1)
    if i == 1:
        print(f"    {a.last_name} scores! {emoji[j]}")
    elif i == 2:
        print(f"    {a.last_name} hits it! {emoji[j]}")
    else:
        print(f"    {a.last_name} makes the shot! {emoji[j]}")


def madelayup(a: Player):
    i: int = randint(1, 3)
    j: int = randint(0, 3)
    sleep(1)
    if i == 1:
        print(f"    {a.last_name} lays it in! {emoji[j]}")
    elif i == 2:
        print(f"    {a.last_name} finishes at the rim! {emoji[j]}")
    elif i == 3:
        print(f"    The layup is good! {emoji[j]}")
    else:
        print(f"    {a.last_name} with the floater! {emoji[j]}")


def madedunk(a: Player):
    i: int = randint(1, 7)
    j: int = randint(0, 3)
    sleep(1)
    if i == 1 or i == 2:
        print(f"    {a.last_name} with the jam! {emoji[j]}")
    elif i == 3 or i == 4:
        print(f"    {a.last_name} with the dunk! {emoji[j]}")
    elif i == 5 or i == 6:
        print(f"    {a.last_name} with the flush! {emoji[j]}")
    else:
        print(f"    {a.last_name} put him on a poster!!! {emoji[j]} {emoji[j]}")


def made3(a: Player):
    i: int = randint(1, 4)
    j: int = randint(0, 3)
    sleep(1)
    if i == 1:
        print(f"    {a.last_name} sinks the three! {emoji[j]}")
    elif i == 2:
        print(f"    {a.last_name}, nothing but net! {emoji[j]}")
    elif i == 3:
        print(f"    {a.last_name} scores! {emoji[j]}")
    elif i == 4:
        print(f"    Bang! {emoji[j]}")
    else:
        print(f"    {a.last_name} nails the three! {emoji[j]}")


def miss(a: Player):
    i: int = randint(1, 4)
    sleep(1)
    if i == 1:
        print(f"    The shot rims out. {MISS}")
    elif i == 2:
        print(f"    {a.last_name} missed. {MISS}")
    elif i == 3:
        print(f"    No good. {MISS}")
    else:
        print(f"    Off the rim. {MISS}")


def madefree(a: Player):
    i: int = randint(1, 4)
    j: int = randint(0, 3)
    sleep(1.5)
    if i == 1:
        print(f"        {a.last_name} makes the free throw! {emoji[j]}")
    elif i == 2:
        print(f"        {a.last_name}, nothing but net! {emoji[j]}")
    elif i == 3:
        print(f"        {a.last_name} scores! {emoji[j]}")
    else:
        print(f"        {a.last_name} knocks down the free throw! {emoji[j]}")


def madepass(a: Player, b: Player):
    i: int = randint(1, 4)
    sleep(1.5)
    if i == 1:
        print(f"    {a.last_name} passes to {b.last_name}.")
    elif i == 2:
        print(f"    {a.last_name} passes it to {b.last_name}.")
    elif i == 3:
        print(f"    {a.last_name} with the feed to {b.last_name}.")
    else:
        print(f"    {a.last_name} finds {b.last_name} with a nice pass.")


def failpass(a: Player, b: Player):
    i: int = randint(1, 3)
    sleep(1.5)
    if i == 1:
        print(f"{b.last_name} intercepts {a.last_name}'s pass!")
    elif i == 2:
        print(f"{a.last_name} gives the ball away.")
    else:
        print(f"Turnover! poor pass from {a.last_name}.")


def shoot2(a: Player, b: Player) -> int:
    chance1: float = round(uniform(0.5, 1.3), 1)
    chance2: float = round(uniform(0.5, 1.3), 1)
    chance3: float = round(uniform(1, 1.5), 1)
    result: int = 0
    shot: int = a.two
    block: int = b.defense
    accuracy: float = randint(46, 99) * chance3
    sleep(1.5)
    print(f"    {a.first_name} {a.last_name} shoots...")
    sleep(1.5)
    a.shots += 1
    whichshot: int = randint(1, 10)
    if whichshot < 2:
        if ((shot + 50) * chance1) > (block * chance2):
            result = 2
            made2(a)
            a.made += 1
            return result
        else:
            print(f"    {b.last_name} blocked the shot!")
            b.blocks += 1
            return result
    else:
        if ((shot + 50) * chance1) > accuracy:
            result = 2
            made2(a)
            a.made += 1
            return result
        else:
            miss(a)
            return result


def shoot3(a: Player, b: Player) -> int:
    chance1: float = round(uniform(0.5, 1.3), 1)
    chance2: float = round(uniform(0.5, 1.3), 1)
    chance3: float = round(uniform(1, 1.5), 1)
    result: int = 0
    shot: int = a.three
    block: int = b.defense
    accuracy: float = randint(46, 99) * chance3
    sleep(1.5)
    print(f"    {a.first_name} {a.last_name} shoots a 3...")
    sleep(1.5)
    a.shots += 1
    whichshot: int = randint(1, 10)
    if whichshot < 2:
        if ((shot + 50) * chance1) > (block * chance2):
            result = 3
            made3(a)
            a.made += 1
            return result
        else:
            print(f"    {b.last_name} blocked the shot!")
            b.blocks += 1
            return result
    else:
        if ((shot + 50) * chance1) > accuracy:
            result = 3
            made3(a)
            a.made += 1
            return result
        else:
            miss(a)
            return result


def layup(a: Player, b: Player) -> int:
    chance1: float = round(uniform(0.5, 1.3), 1)
    chance2: float = round(uniform(0.5, 1.3), 1)
    result: int = 0
    shot: int = a.two
    block: int = b.defense
    sleep(1.5)
    a.shots += 1
    if ((shot + 50) * chance1) > (block * chance2):
        result = 2
        madelayup(a)
        a.made += 1
        return result
    else:
        print(f"    {b.last_name} blocks {a.last_name} at the rim!")
        b.blocks += 1
        return result


def dunk(a: Player, b: Player) -> int:
    chance1: float = round(uniform(0.5, 1.3), 1)
    chance2: float = round(uniform(0.5, 1.3), 1)
    result: int = 0
    shot: int = a.two
    ajump: int = a.jump
    bjump: int = b.jump
    block: int = b.defense
    sleep(1.5)
    a.shots += 1
    if ((shot + ajump) * chance1) > ((block + bjump) * chance2):
        result = 2
        madedunk(a)
        a.made += 1
        return result
    else:
        print(f"    {b.last_name} denies {a.last_name}! {MISS}")
        b.blocks += 1
        return result


def freethrow(a: Player) -> int:
    chancea: float = round(uniform(0.5, 1.5), 1)
    chanceb: float = round(uniform(0.5, 1.5), 1)
    chance2: int = randint(1, 99)
    chance3: int = randint(1, 99)
    shot1: float = round(uniform(0.5, 1.5), 1) * chance2
    shot2: float = round(uniform(0.5, 1.5), 1) * chance3
    shota: float = a.free * chancea
    shotb: float = a.free * chanceb
    result: int = 0
    a.shots += 2
    if shota > shot1:
        madefree(a)
        a.made += 1
        result += 1
    else:
        sleep(1.5)
        miss(a)
    if shotb > shot2:
        madefree(a)
        a.made += 1
        result += 1
    else:
        sleep(1.5)
        miss(a)
    sleep(1)
    return result