"""Unit tests for dictionary functions."""

from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730394262"


# unit tests for invert
def test_invert_empty() -> None:
    """Tests invert when the given dictionary is empty."""
    xs: dict[str, str] = {}
    assert invert(xs) == {}


def test_invert_1() -> None:
    """Tests invert using a dictionary of letters."""
    xs: dict[str, str] = {'a': 'b', 'c': 'd', 'e': 'f'}
    assert invert(xs) == {'b': 'a', 'd': 'c', 'f': 'e'}


def test_invert_2() -> None:
    """Tests invert using a dictionary of words that logically follow each other."""
    xs: dict[str, str] = {'second': 'first', 'fourth': 'third', 'sixth': 'fifth'}
    assert invert(xs) == {'first': 'second', 'third': 'fourth', 'fifth': 'sixth'}


# unit tests for favorite_color
def test_favorite_empty() -> None:
    """Tests favorite color when the dictionary is empty."""
    xs: dict[str, str] = {}
    assert favorite_color(xs) == ""


def test_favorite_color_1() -> None:
    """Tests favorite_color with a dict of people and their favorite cars."""
    xs: dict[str, str] = {'ben': 'toyota', 'bill': 'honda', 'bob': 'toyota'}
    assert favorite_color(xs) == 'toyota'


def test_favorite_color_2() -> None:
    """Tests favorite_color with a dict with a tie at the top."""
    xs: dict[str, str] = {'ben': 'green', 'bill': 'blue', 'bob': 'yellow'}
    assert favorite_color(xs) == 'green'


# unit tests for count
def test_count_empty() -> None:
    """Tests count wiht an empty list."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_1() -> None:
    """Tests count for a list of donut flavors."""
    xs: list[str] = ['glazed', 'boston creme', 'glazed', 'cinnamon', 'boston creme', 'boston creme']
    assert count(xs) == {'glazed': 2, 'boston creme': 3, 'cinnamon': 1}


def test_count_2() -> None:
    """Tests count for football teams that have won superbowls."""
    xs: list[str] = ['packers', 'bears', 'patriots', 'patriots', 'broncos', 'packers', 'steelers', 'steelers', 'patriots']
    assert count(xs) == {'packers': 2, 'bears': 1, 'patriots': 3, 'broncos': 1, 'steelers': 2}