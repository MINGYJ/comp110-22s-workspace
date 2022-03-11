"""Test of the dictionary functions."""
__author__ = "730486611"


from dictionary import invert, favorite_color, count


def test_favorite_color() -> None:
    """Test the favorite color."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_count() -> None:
    """Test case of count function."""
    assert count(["a", "a", "c", "b", "a", "b"]) == {'a': 3, 'c': 1, 'b': 2}


def test_invert() -> None:
    """Test of edge case--Key Error."""
    invert({'kris': 'jordan', 'michael': 'jordan'}) 