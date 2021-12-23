"""Drawing forests in a loop."""

__author__ = "730484862"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

output: str = ""
i: int = 0
j: int = 0

user_depth: int = int(input("Depth: "))

while i < user_depth:
    output = output + TREE
    print(output)
    i = i + 1
    