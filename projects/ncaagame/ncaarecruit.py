"""Recruit a set of random players."""

__author__ = "Gianluca Ciuffreda"

from random import randint
from projects.basket import Player, make_PG, make_SG, make_SF, make_PF, make_C

i: int = 0
while i < 3:
    r: int = randint(0, 4)
    if r == 0:
        x: Player = make_PG()
        x.read()
        x.readme()
    elif r == 1:
        x: Player = make_SG()
        x.read()
        x.readme()
    elif r == 2:
        x: Player = make_SF()
        x.read()
        x.readme()
    elif r == 3:
        x: Player = make_PF()
        x.read()
        x.readme()
    else:
        x: Player = make_C()
        x.read()
        x.readme()
    i += 1