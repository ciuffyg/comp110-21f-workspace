"""A Basketball Program."""

__author__ = "Gianluca Ciuffreda"


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


class Team:
    """Defines a team and their attributes."""
    name: str
    roster: list[Player]

    def __init__(self, a: str):
        self.name = a
        self.roster = []

    def __repr__(self) -> str:
        return self.name


def max_play(l1: list[Player]) -> float:
    if len(l1) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    maxval: float = l1[i].play
    while i < len(l1):
        if l1[i].play > maxval:
            maxval = l1[i].play
        i += 1
    return maxval


def min_play(l1: list[Player]) -> float:
    if len(l1) == 0:
        raise ValueError("min() arg is an empty List")
    i: int = 0
    minval: float = l1[i].play
    while i < len(l1):
        if l1[i].play < minval:
            minval = l1[i].play
        i += 1
    return minval