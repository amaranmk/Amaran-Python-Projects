"""Finding duplicate letters in a word."""

__author__ = "730484862"

user_input: str = input("Enter a word: ")
i: int = 0
j: int = 0
dup_counter: int = 0

while i < len(user_input):
    while j < len(user_input):
        if i != j:
            if user_input[j] == user_input[i]:
                dup_counter = dup_counter + 1
                j = j + 1
            else:
                j = j + 1
        else:
            j = j + 1
    i = i + 1
    j = 0
    
if dup_counter >= 1:
    print("Found duplicate: True")
else:
    print("Found duplicate: False")
