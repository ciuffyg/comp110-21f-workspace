"""A Practice File."""

__author__ = "730394262"


def main() -> None:
    boo(tricks)


def boo(kvs: dict[str, int]) -> list[int]:
    r: list[int] = []
    for k in kvs:
        r.append(kvs[k])
    return r


tricks: dict[str, int] = {"trick": 211, "or": 210, "treat": 110}

if __name__ == "__main__":
    main()