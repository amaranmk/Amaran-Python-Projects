"""Example of a function that processes a list."""

__author__ = "730484862"


def main() -> None:
    names: list[str] = ["Kris", "Kaki"]
    print(contains("Kris", names))


# Define a function named contains
# We can give two arguments: a needle value we're searching for in a haystack list
def contains(needle: str, haystack: list[str]) -> bool:
    """Return True if needle is found in haystack, False otherwise."""
    # Return true if needle is found in haystack, false otherwise
    # Loop through each index in list
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
            # Test if item stored at index is equal to needle
            # Return true if so
            return True
        i += 1
    # Return false after testing each item
    return False


# Python Idiom for starting the main funciton
if __name__ == "__main__":
    main()
