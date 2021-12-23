"""Repeating a beat in a loop."""

__author__ = "730484862"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
i: int = 0
repeat: int = int(input("How many times do you want to repeat it? "))
beat_output: str = ""

if repeat > 0:
    while i < repeat:
        beat_output = beat_output + beat
        if i < repeat - 1:
            beat_output = beat_output + " "
            i = i + 1
        else:
            i = i + 1
            print(beat_output) 
else:
    print("No beat...")
