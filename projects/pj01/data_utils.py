"""Utility Functions."""

__author__ = "730394262"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)

    return result
    

def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
        
    return result


def head(xs: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first n rows of data for each column."""
    result: dict[str, list[str]] = {}

    for column in xs:
        if n >= len(xs[column]):
            n = len(xs[column])
        row_list: list[str] = []
        i: int = 0
        while i < n:
            row_list.append(xs[column][i])
            i += 1
        result[column] = row_list

    return result


def select(xs: dict[str, list[str]], ys: list[str]) -> dict[str, list[str]]:
    """Produces a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}

    i: int = 0
    while i < len(ys):
        result[ys[i]] = []
        i += 1
    
    for column in result:
        result[column] = xs[column]

    return result


def concat(xs: dict[str, list[str]], ys: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}

    for column in xs:
        result[column] = xs[column]
    for column in ys:
        if column in result:
            i: int = 0
            while i < len(ys[column]):
                result[column].append(ys[column][i])
                i += 1
        else:
            result[column] = ys[column]

    return result


def count(xs: list[str]) -> dict[str, int]:
    """Produces a dict[str, int] where each key is a unique value in a given list and each value is the frequency that value appears in the list."""
    result: dict[str, int] = {}
    i: int = 0
    while i < len(xs):
        if xs[i] in result:
            result[xs[i]] += 1
        else:
            result[xs[i]] = 1
        i += 1

    return result


def countint(xs: list[int]) -> dict[int, int]:
    """Based on count function. Produces a dict[int, int] where each key is a unique value in a given list and each value is the frequency that value appears in the list."""
    result: dict[int, int] = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
    i: int = 0
    while i < len(xs):
        if xs[i] in result:
            result[xs[i]] += 1
        else:
            result[xs[i]] = 1
        i += 1

    return result


def disagree_helper(xs: list[int], maxi: int) -> dict[int, int]:
    """Creates a dict[int, int] where keys are unique values in a given list that are less than the maxi parameter and each value is the frequency that value appears in the list."""
    result: dict[int, int] = {}
    i: int = 0
    while i < len(xs):
        if xs[i] < maxi:
            if xs[i] in result:
                result[xs[i]] += 1
            else:
                result[xs[i]] = 1
            i += 1
        else:
            i += 1

    return result