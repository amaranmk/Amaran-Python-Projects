"""List utility functions."""

__author__ = "730484862"


# TODO: Implement your functions here.
def all(numlist: list[int], ind_num: int) -> bool:
    """Checks if the integer given matches the value in every index of the list given."""
    if len(numlist) == 0:
        return False
    else:
        i: int = 0
        while i < len(numlist):
            if ind_num != numlist[i]:
                return False
            else:
                i += 1
    return True


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Checks if every value in the corresponding index of both given lists match."""
    if len(first_list) != len(second_list):
        return False
    i: int = 0
    while i < len(first_list):
        if first_list[i] != second_list[i]:
            return False
        else:
            i += 1
    return True


def max(num_list: list[int]) -> int:
    """Returns the highest integer value in the inputted list."""
    i: int = 0
    if len(num_list) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        num_max: int = num_list[i]
        while i < len(num_list):
            if num_max == num_list[i]:
                i += 1
            else:
                if num_max > num_list[i]:
                    i += 1
                else:
                    num_max = num_list[i]
                    i += 1
    return num_max