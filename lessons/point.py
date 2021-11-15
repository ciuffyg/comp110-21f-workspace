"""Example of a Point class."""
from __future__ import annotations

__author__ = "730394262"


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Initializes a point with its x ,y components."""
        self.x = x
        self.y = y
    
    def scale_by(self, factor: float) -> None:
        """Mutates: multiplies components by a factor."""
        self.x *= factor
        self.y *= factor

    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operator for Point * float."""
        return Point(self.x * factor, self.y * factor)

    def scale(self, factor: float) -> Point:
        """Pure method that does not mutate the point."""
        return Point(self.x * factor, self.y * factor)
    
    def __str__(self) -> str:
        """Produce a str representation of a point for humans."""
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Produce a str representation of a Point for Python!"""
        return f"Point({self.x}, {self.y})"

    def __add__(self, rhs: Point) -> Point:
        """Overload the addition operator for Point + Point."""
        print("__add__ was called")
        return Point(self.x + rhs.x, self.y + rhs.y)

    def __getitem__(self, index: int) -> float:
        """Overload using indexes with a Point object."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError


p0: Point = Point(1.0, 2.0)
p0.scale_by(2.0)
# print(f"{p0.x}, {p0.y}")
p1: Point = p0.scale(2.0)
# print(f"{p1.x}, {p1.y}")
print(p0)
print(p1)
p1_as_a_str: str = str(p1)
print(p1_as_a_str)

p1_repr: str = repr(p1)
print(p1_repr)

a: Point = Point(1.0, 2.0)
b: Point = a * 2.0
c: Point = a + b
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

print(a[0])
print(a[1])