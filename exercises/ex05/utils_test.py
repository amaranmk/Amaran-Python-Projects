"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730484862"


# only-evens function tests
def test_only_evens_empty() -> None:
    """Tests empty list."""
    list_input: list[int] = []
    assert only_evens(list_input) == []


def test_only_evens_no_evens() -> None:
    """Tests list with no evens."""
    list_input: list[int] = [1, 5, 3]
    assert only_evens(list_input) == []


def test_only_evens_all_evens() -> None:
    """Tests list with all evens."""
    list_input: list[int] = [4, 4, 4]
    assert only_evens(list_input) == [4, 4, 4]


# sub function tests
def test_sub_empty() -> None:
    """Tests empty list."""
    list_input: list[int] = []
    start_index: int = 0
    end_index: int = 3 
    assert sub(list_input, start_index, end_index) == []


def test_sub_middle() -> None:
    """Tests outputting middle of list."""
    list_input: list[int] = [10, 20, 30, 40]
    start_index: int = 1
    end_index: int = 3
    assert sub(list_input, start_index, end_index) == [20, 30]


def test_sub_end_large() -> None:
    """Tests an end index greater than the list length."""
    list_input: list[int] = [43, 42, 4]
    start_index: int = 1
    end_index: int = 5
    assert sub(list_input, start_index, end_index) == [42, 4]


# concat function tests
def test_concat_empty() -> None:
    """Tests empty list."""
    first_list: list[int] = []
    second_list: list[int] = [43, 42, 4]
    assert concat(first_list, second_list) == [43, 42, 4]


def test_concat_first_second() -> None:
    """Tests standard concat use case."""
    first_list: list[int] = [43, 42, 47, 6, 53]
    second_list: list[int] = [43, 42, 4, 3]
    assert concat(first_list, second_list) == [43, 42, 47, 6, 53, 43, 42, 4, 3]


def test_concat_negative() -> None:
    """Tests concatonating with a negative int."""
    first_list: list[int] = [43, 42, 4]
    second_list: list[int] = [43, 42, 4, -8, 9]
    assert concat(first_list, second_list) == [43, 42, 4, 43, 42, 4, -8, 9]