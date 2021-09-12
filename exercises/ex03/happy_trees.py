"""Drawing forests in a loop."""

__author__ = "730394262"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
dep: int = int(input("Depth: "))
i: int = 0

while i < dep:
    print(TREE)
    i = i + 1
    TREE = TREE + '\U0001F332'