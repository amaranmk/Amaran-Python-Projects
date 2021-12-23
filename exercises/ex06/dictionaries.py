"""Practice with dictionaries."""

__author__ = "730484862"


# Define your functions below
def invert(pre_invert: dict[str, str]) -> dict[str, str]:
    """Function that inverts the keys and values of an inputted dict."""
    inverted_dict: dict[str, str] = dict()
    for key_pre in pre_invert:
        if len(inverted_dict) > 0:
            for key_invert in inverted_dict:
                if pre_invert[key_pre] == key_invert:
                    raise KeyError("Duplicate key")
            inverted_dict[pre_invert[key_pre]] = key_pre
        else:
            inverted_dict[pre_invert[key_pre]] = key_pre
    return inverted_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Function that returns the most popular color from an inputted dict."""
    color_tracker: dict[str, int] = dict()
    i: int = 0
    highest_color: str = ""
    for person in input_dict:
        if input_dict[person] in color_tracker:
            color_tracker[input_dict[person]] += 1
        else:
            color_tracker[input_dict[person]] = 1
    for tracker_color in color_tracker:
        if i < 1:
            highest_color = tracker_color
            i += 1
        else:
            if color_tracker[tracker_color] > color_tracker[highest_color]:
                highest_color = tracker_color
    return highest_color


def count(input_list: list[str]) -> dict[str, int]:
    """Function that creates dict with items from a list and their frequency."""
    dict_tracker: dict[str, int] = dict()
    for item in input_list:
        if item in dict_tracker:
            dict_tracker[item] += 1
        else:
            dict_tracker[item] = 1
    return dict_tracker