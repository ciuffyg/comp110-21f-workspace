"""Practice with dictionaries."""

__author__ = "730394262"


def main() -> None:
    """This is the main function."""
    print(invert(dict_1))
    print(favorite_color(dict_2))
    print(count(list_1))


dict_1: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
dict_2: dict[str, str] = {'Marc': 'yellow', 'Ezri': 'green', 'Kris': 'blue', 'Alex': 'green', 'John': 'blue', 'Jack': 'blue'}
list_1: list[str] = ['chicken', 'pork', 'pork', 'beef', 'pork', 'chicken']


def invert(ds: dict[str, str]) -> dict[str, str]:
    """Returns a disctionary of type str, str when given a dictionary of type str, str."""
    invt_ds: dict[str, str] = {}
    x: str = ""
    for key in ds:
        x = ds[key]
        invt_ds[x] = key
    return invt_ds


def favorite_color(ds: dict[str, str]) -> str:
    """Retuns the favorite color in a dictionary or the first color in the dictionary if there is a tie."""
    popular: str = ""
    popcount: int = 0
    count_list: list[str] = list()
    for key in ds:
        count_list.append(ds[key])
    # print(count_list)
    g: int = 0
    while g < len(count_list):
        i: int = 0
        localpopct: int = 0
        localpopular: str = count_list[g]
        while i < len(count_list):
            if count_list[i] == localpopular:
                localpopct += 1
            i += 1
        if localpopct > popcount:
            popular = localpopular
            popcount = localpopct
        g += 1
    return popular


def count(xs: list[str]) -> dict[str, int]:
    """Returns a dictionary with the str values from a given lsit as keys and their corresponding values as their frequency in the list."""
    count_dict: dict[str, int] = {}
    i: int = 0
    while i < len(xs):
        if xs[i] in count_dict:
            count_dict[xs[i]] += 1
        else:
            count_dict[xs[i]] = 1
        i += 1
    return count_dict


if __name__ == "__main__":
    main()