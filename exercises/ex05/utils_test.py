"""Unit tests for list utility functions."""


__author__ = "730394262"

from exercises.ex05.utils import only_evens, sub, concat


# only_evens tests
def test_list_empty() -> None:
    xs: list[int] = list()
    assert only_evens(xs) == list()


def test_list_evens() -> None:
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_list_evens_2() -> None:
    xs: list[int] = [234, 23, 44, 46, 97, 87, 10]
    assert only_evens(xs) == [234, 44, 46, 10]


# sub tests
def test_empty_params() -> None:
    xs: list[int] = list()
    a: int = 1
    b: int = 5
    assert sub(xs, a, b) == list()


def test_sub() -> None:
    xs: list[int] = [12, 88, 87, 83, 81, 1, 2, 44, 59]
    a: int = 1
    b: int = 7
    assert sub(xs, a, b) == [88, 87, 83, 81, 1, 2]


def test_sub_1() -> None:
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    a: int = 0
    b: int = 4
    assert sub(xs, a, b) == [1, 2, 3, 4]


# concat tests
def test_empty_lists() -> None:
    xs: list[int] = list()
    ys: list[int] = list()
    assert concat(xs, ys) == list()


def test_concat() -> None:
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    ys: list[int] = list()
    assert concat(xs, ys) == [1, 2, 3, 4, 5, 6]


def test_concat_1() -> None:
    xs: list[int] = [1, 2, 3, 4]
    ys: list[int] = [5, 6, 7, 8]
    assert concat(xs, ys) == [1, 2, 3, 4, 5, 6, 7, 8]