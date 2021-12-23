"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730484862"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
random_integer: int = randint(0, 3)

print("Your fortune cookie says...")
if random_integer == 0:
    print("Your shoes will make you happy today.")
else:
    if random_integer == 1:
        print("Fortune favors the brave.")
    else:
        if random_integer == 2:
            print("Life consists not in holding good cards, but in playing those you hold well.")
        else:
            print("You are very talented in many ways.")

print("Now, go spread positive vibes!")
