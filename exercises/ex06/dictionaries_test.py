"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import count, favorite_color, invert  # , favorite_color, count
import pytest

__author__ = "730484862"


# invert function tests
def test_invert_empty() -> None:
    """Tests empty dict."""
    pre_invert: dict[str, str] = {}
    assert invert(pre_invert) == {}


def test_invert_standard() -> None:
    """Tests standard dict."""
    pre_invert: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(pre_invert) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_one() -> None:
    """Tests dict with one key and value."""
    pre_invert: dict[str, str] = {'apple': 'cat'}
    assert invert(pre_invert) == {'cat': 'apple'}


with pytest.raises(KeyError):
    pre_invert = {'kris': 'jordan', 'michael': 'jordan'}
    invert(pre_invert)


# favorite_color function tests
def test_favorite_color_empty() -> None:
    """Tests empty dict."""
    input_dict: dict[str, str] = {}
    assert favorite_color(input_dict) == ""


def test_favorite_color_standard() -> None:
    """Tests standard dict."""
    input_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(input_dict) == "blue"


def test_favorite_color_duplicate() -> None:
    """Tests dict with tie."""
    input_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "green", "Kris": "green", "Sam": "blue", "Joe": "blue"}
    assert favorite_color(input_dict) == "green"


# count function tests
def test_count_empty() -> None:
    """Tests empty list."""
    input_list: list[str] = []
    assert count(input_list) == {}


def test_count_standard() -> None:
    """Tests standard list."""
    input_list: list[str] = ["yellow", "blue", "green"]
    assert count(input_list) == {"yellow": 1, "blue": 1, "green": 1}


def test_count_multiples() -> None:
    """Tests list with multiples."""
    input_list: list[str] = ["yellow", "blue", "blue", "green", "green", "green"]
    assert count(input_list) == {"yellow": 1, "blue": 2, "green": 3}