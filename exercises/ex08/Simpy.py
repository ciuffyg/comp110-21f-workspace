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

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
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
        result: float = 0.0
        floatz: list[float] = self.values
        i: int = 0
        while i < len(floatz):
            result += floatz[i]
            i += 1
        return result

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for addition."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
            return result
        else:
            for value in self.values:
                result.values.append(value + rhs)
            return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for power."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
            return result
        else:
            for value in self.values:
                result.values.append(value ** rhs)
            return result

    def __eq__(self, threshold: Union[float, Simpy]) -> list[bool]:
        """Operator overload for equals."""
        result: list[bool] = []
        if isinstance(threshold, float):
            for item in self.values:
                if item == threshold:
                    result.append(True)
                else:
                    result.append(False)
            return result
        else:
            assert len(self.values) == len(threshold.values)
            i: int = 0
            for item in self.values:
                if item == threshold.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
            return result

    def __gt__(self, threshold: Union[float, Simpy]) -> list[bool]:
        """Operator overload for greater than."""
        result: list[bool] = []
        if isinstance(threshold, float):
            for item in self.values:
                if item > threshold:
                    result.append(True)
                else:
                    result.append(False)
            return result
        else:
            assert len(self.values) == len(threshold.values)
            i: int = 0
            for item in self.values:
                if item > threshold.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
            return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Operator overload for subscription notation."""
        if isinstance(rhs, int):
            result_fl: float = self.values[rhs]
            return result_fl
        else:
            result: Simpy = Simpy([])
            i: int = 0
            while i < len(self.values):
                if rhs[i] is True:
                    result.values.append(self.values[i])
                    i += 1
                else:
                    i += 1
            return result