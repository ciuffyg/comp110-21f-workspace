"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730394262"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        """Constructor definition for initializing value attributes."""
        self.values = values

    def __str__(self) -> str:
        """Simple __str__ method that automatically returns a str when Simpy is called."""
        return f"Simpy({self.values})"

    def fill(self, filler: float, filled: int) -> None:
        """Procedure-like method that returns none and mutates the data by filling in floats."""
        result: list[float] = []
        repeat: int = filled
        while repeat > 0:
            result.append(filler)
            repeat -= 1
        self.values = result

    def arange(self, start: float, stop: float, step: float = 1.0) -> str:
        """Fills values from start to stop in increments of 1.0 unless otherwise specified."""
        assert step != 0
        result: list[float] = [start]
        begin: float = start
        while begin + step != stop:
            begin += step
            result.append(begin)
        self.values = result

    def sum(self) -> float:
        """Computes and returns the sum of all floats in the values attribute."""