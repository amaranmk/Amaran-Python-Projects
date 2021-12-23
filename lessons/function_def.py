"""An example function definition."""

__author__ = "730484862"


def my_max(a: int, b: int) -> int:
    """Returns the largest argument."""
    if a >= b:
        return a 
    else:
        return b


x: int = 6
y: int = 5 + 2
z: int = my_max(x, y)
print(z)
