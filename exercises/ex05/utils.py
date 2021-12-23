"""List utility functions part 2."""

__author__ = "730484862"


# Define your functions below
def only_evens(list_input: list[int]) -> list[int]:
    """Returns only the elements of the list that were even."""
    i: int = 0
    even_list: list[int] = list()
    while i < len(list_input):
        if (list_input[i] % 2) == 0:
            even_list.append(list_input[i])
            i += 1
        else:
            i += 1
    return even_list


def sub(list_input: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns a subset of the inputted list based on the inputted start index and end index."""
    i: int = 0
    if start_index > 0:
        i = start_index
    if end_index > len(list_input):
        end_index = len(list_input)
    subset_list: list[int] = list()

    if len(list_input) == 0 or start_index > len(list_input) or end_index <= 0:
        return subset_list
    else:
        while i < end_index:
            subset_list.append(list_input[i])
            i += 1
    return subset_list


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Returns a list with the all the elements of the first list followed by the elements of the second list."""
    i: int = 0
    j: int = 0
    concatenated_list: list[int] = list()
    if len(first_list) > 0:
        while i < len(first_list):
            concatenated_list.append(first_list[i])
            i += 1
    if len(second_list) > 0:
        while j < len(second_list):
            concatenated_list.append(second_list[j])
            j += 1
    return concatenated_list
