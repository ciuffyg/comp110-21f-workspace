"""List utility functions part 2."""

__author__ = "730394262"


def main() -> None:
    """This is the main function."""
    testlist: list[int] = [1, 3, 5, 2, 4, 60]
    testlist2: list[int] = [90, 45, 13, 10]
    print(only_evens(testlist))
    print(sub(testlist, 1, 5))
    print(concat(testlist, testlist2))


def only_evens(xs: list[int]) -> list[int]:
    """Returns all even items when given a list of ints."""
    evens: list[int] = list()
    if xs != list():
        i: int = 0
        while i < len(xs):
            if xs[i] % 2 == 0:
                evens.append(xs[i])
            i += 1
        return evens
    return list()


def sub(xs: list[int], istart: int, iend: int) -> list[int]:
    """Returns a subset of a list when given a list, start index, and end index."""
    subset: list[int] = list()
    index: int = istart
    if istart <= len(xs):
        raise IndexError("list index out of range")
    if xs != list():
        while index < iend:
            subset.append(xs[index])
            index += 1
        return subset
    return list()


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """When given two lists of ints, returns the first list and then the second list together."""
    both: list[int] = list()
    both = xs + ys
    return both


if __name__ == "__main__":
    main()