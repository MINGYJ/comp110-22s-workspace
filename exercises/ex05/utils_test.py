"""The test program for utils."""


__author__ = "730486611"


from utils import only_evens, sub, concat


A_LIST = ([1, 2, 3, 4, 5, 6, 7, 8, 9])
B_LIST = ([10, 11, 20, 30, 33, 40, 50, 55])


def main() -> None:
    """The main function use to run all test functions."""
    print(test_concat_even())
    print(test_even_sub())
    print(test_double_sub())


def test_concat_even() -> list[int]:
    """Add the even part of two list."""
    return concat(only_evens(A_LIST), only_evens(B_LIST))


def test_even_sub() -> list[int]:
    """A function return the even element in a sublist."""
    start: int = -10
    end: int = 6
    return only_evens(sub(A_LIST, start, end))


def test_double_sub() -> list[int]:
    """A function return a list contains a sublist twice."""
    start: int = 1
    end: int = 6
    return concat(sub(B_LIST, start, end), sub(B_LIST, start, end))


if __name__ == "__main__":
    main()