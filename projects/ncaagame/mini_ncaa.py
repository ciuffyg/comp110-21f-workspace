"""A Basketball Program."""

__author__ = "Gianluca Ciuffreda"


from random import randint

firstname: list[str] = ["John", "Brady", "Caleb", "Leroy", "DeAndre", "Demar", "Luka", "Armando", "George", "RJ", "Jalen", "DJ", "Derrick", "Erik", "Daniel", "Tom", "Michael", "Russell", "Chris", "Kevin", "Dwayne", "Kyrie", "Damian", "Karl", "Carmelo", "Steve", "Jack", "Alejandro", "Bill", "Hubert", "Mike", "Steph", "Jalen", "Miles", "Devin", "TJ", "AJ", "CJ", "Bud", "Giovanni", "Stefano", "Marco", "Jeremy", "Yao", "Mohamed", "Ibrahim", "Ahmed", "Cho", "Juan", "Carlos", "Luis", "Brook", "Kemba", "Tyler", "Ty", "Al", "Anthony", "Burton", "Cameron", "Cory", "Clark", "Hugo", "Cole", "Reggie", "Grayson", "DeMarcus", "Bruno", "Denis", "Mario", "Ben", "Shawn", "Raymond", "Frank", "Rechon", "Malik", "Jake", "Mo", "Dwight", "Draymond", "Aaron", "Trevor", "Charlie", "Gary", "Jimmy"]
lastname: list[str] = ["Jefferson", "Brady", "Brown", "Smith", "Williams", "DeRozan", "James", "Bacot", "Jordan", "Davis", "Lee", "Murray", "Allen", "Anthony", "Paul", "Irving", "Doncic", "Wade", "Jones", "Curry", "Johnson", "Durant", "Nash", "Thomas", "Ball", "Pierce", "Black", "White", "Villanueva", "Walton", "McCoy", "MacIntosh", "Austin", "Young", "Bridges", "Silva", "Morris", "Morrison", "Santos", "Romano", "Russo", "Bianco", "Lin", "Ming", "Ali", "Adebayo", "Mensah", "Chen", "Garcia", "Lopez", "Gonzalez", "Sanchez", "Adams", "Robinson", "Walker", "Harris", "Guster", "Lewis", "Payne", "Knight", "Green", "Jenkins", "Carter", "Miller", "Bush", "Cousins", "Jokic", "Morant", "Wilkins", "Chamberlain", "Love", "Jin", "Cosby", "Howard", "Gardner", "Fox", "Ward", "Hart", "Butler"]
colleges: list[str] = ["Gonzaga", "Georgia St", "Boise St", "Memphis", "Uconn", "New Mexico St", "Arkansas", "Vermont", "Alabama", "Notre Dame", "Texas Tech", "Montana St", "Michigan St", "Davidson", "Duke", "CSU Fullerton", "Baylor", "Norfolk St", "North Carolina", "Marquette", "Saint Mary's", "Indiana", "UCLA", "Texas", "Virginia Tech", "Purdue", "Yale", "Murray St", "San Francisco", "Kentucky", "Saint Peter's", "Arizona", "Wichita St", "Seton Hall", "TCU", "Houston", "Oregon", "Illinois", "Xavier", "Colorado St", "Michigan", "Tennessee", "Syracuse", "Ohio State", "Loyola Chicago", "Villanova", "Delaware", "Kansas", "NC State", "San Diego St", "Creighton", "Iowa", "Richmond", "Providence", "S Dakota St", "LSU", "Iowa St", "Wisconsin", "Colgate", "USC", "Miami", "Auburn", "Louisville", "Boston College"]


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
    e: int = randint(floor - 5, floor + 10)
    f: int = randint(floor, ceiling)
    g: int = randint(floor, ceiling)
    h: int = randint(floor - 5, floor + 10)
    j: int = randint(floor - 5, floor + 10)

    end: Player = Player(p, a, b, i, c, d, e, f, g, h, j)
    end.overall()
    return end


def make_SG() -> Player:
    p: str = "SG"
    a: str = firstname[randint(0, 83)]
    b: str = lastname[randint(0, 78)]

    floor: int = randint(1, 34)
    ceiling: int = floor + 15

    i: float = 0.0
    c: int = randint(floor - 5, floor + 10)
    d: int = randint(floor, ceiling)
    e: int = randint(floor, ceiling)
    f: int = randint(floor, ceiling)
    g: int = randint(floor, ceiling)
    h: int = randint(floor - 5, floor + 10)
    j: int = randint(floor - 5, floor + 10)

    end: Player = Player(p, a, b, i, c, d, e, f, g, h, j)
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
    e: int = randint(floor - 5, floor + 10)
    f: int = randint(floor - 5, floor + 10)
    g: int = randint(floor, ceiling)
    h: int = randint(floor - 5, floor + 10)
    j: int = randint(floor, ceiling)

    end: Player = Player(p, a, b, i, c, d, e, f, g, h, j)
    end.overall()
    return end


def make_PF() -> Player:
    p: str = "PF"
    a: str = firstname[randint(0, 83)]
    b: str = lastname[randint(0, 78)]

    floor: int = randint(1, 34)
    ceiling: int = floor + 15

    i: float = 0.0
    c: int = randint(floor - 5, floor + 10)
    d: int = randint(floor, ceiling)
    e: int = randint(floor - 5, floor + 10)
    f: int = randint(floor - 5, floor + 10)
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
    d: int = randint(floor - 5, floor + 10)
    e: int = randint(floor - 5, floor + 10)
    f: int = randint(floor - 5, floor + 10)
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


build_team()
i: int = 0
# while i < 64:
#     print(f"{ncaa_teams[i].readroster()}")
#     i += 1
print(f"{ncaa_teams[i].readroster()}")


# def match(hpg: Player, hsg: Player, hsf: Player, hpf: Player, hc: Player, apg: Player, asg: Player, asf: Player, apf: Player, ac: Player):
#     clock: int = 100
#     while clock > 0:
