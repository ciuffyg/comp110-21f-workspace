"""A Practice File."""

# from typing import Union

__author__ = "730394262"


def main() -> None:
    lists: list[int] = [1, 2, 3]
    print(reverse_multiply(lists))


def reverse_multiply(xs: list[int]) -> list[int]:
    result: list[int] = []
    i: int = 0
    while i < len(xs):
        item = xs[len(xs) - i]
        result.append(item)
        i += 1
    return result


if __name__ == "__main__":
    main()