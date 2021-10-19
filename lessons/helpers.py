"""Example of functions imported elsewhere."""

__author__ = "730394262"


THE_ANSWER: int = 42


def main() -> None:
    print(powerful(2, 16))
    print(f"helpers.py: {__name__}")
    print("Evaluated as a program.")


def powerful(x: float, n: float) -> float:
    """Raises x to the power of n."""
    return x ** n


if __name__ == "__main__":
    main()
else:
    print("Evaluated as an imported module.")

print(f"helpers.py: {__name__}")