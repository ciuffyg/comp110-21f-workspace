"""List utility functions."""

__author__ = "730394262"


def main() -> None:
    listall: list[int] = [1, 1, 1]
    print(all(listall, 2))
    listone: list[int] = [1, 2, 3]
    listtwo: list[int] = [1, 2, 3]
    print(is_equal(listone, listtwo))
    listmax: list[int] = [2, 10, 8, 10, 11]
    print(max(listmax))


def all(xs: list[int], look: int) -> bool:
    """Returns True if all items in the list are equal to the variable named look, False otherwise."""
    i: int = 0
    itemct: int = 0
    while i < len(xs):
        if xs[i] == look:
            itemct += 1
        i += 1
    if itemct == len(xs):
        return True
    return False


def is_equal(l1: list[int], l2: list[int]) -> bool:
    """Returns True if every item at every index of two lists of ints are equal, False otherwise."""
    i: int = 0
    pairct: int = 0
    while i < len(l1) and i < len(l2):
        if l1[i] == l2[i]:
            pairct += 1
        i += 1
    if pairct == len(l1):
        return True
    return False


def max(l1: list[int]) -> int:
    """Returns the maximun value of a list of ints, returns ValueError if list is empty."""
    if len(l1) == 0:
        raise ValueError("max() arg is an empty List")
    maxval: int = 0
    i: int = 0
    while i < len(l1):
        if l1[i] > maxval:
            maxval = l1[i]
        i += 1
    return maxval


if __name__ == "__main__":
    main()