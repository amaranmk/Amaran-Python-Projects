"""An exercise in remainders and boolean logic."""

__author__ = "730484862"


# Begin your solution here...
user_integer: int = int(input("Enter an int: "))
divisble_by_two: int = user_integer % 2
divisble_by_seven: int = user_integer % 7

if divisble_by_two == 0:
    if divisble_by_seven == 0:
        print("TAR HEELS")
    else:
        print("TAR")
else:
    if divisble_by_seven == 0:
        print("HEELS")

if divisble_by_seven != 0:
    if divisble_by_two != 0:
        print("CAROLINA")
