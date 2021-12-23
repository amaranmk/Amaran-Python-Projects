"""Choose Your Own Adventure PJ00."""

__author__ = "730484862"

from random import choice

# The string constant for the various emojis used
SLOT_MACHINE: str = '\U0001F3B0'
PURPLE_FACE: str = '\U0001F608'
SUNGLASS_FACE: str = '\U0001F60E'
HOT_FACE: str = '\U0001F975'
CHICK: str = '\U0001F425'
LION: str = '\U0001F3B0'
OCTOPUS: str = '\U0001F981'
DOOR: str = '\U0001F6AA'
MONEY_FACE: str = '\U0001F911'
MONEY_BAG: str = '\U0001F4B0'
SAD_FACE: str = '\U0001F615'
WAVING_HAND: str = '\U0001F44B'
CONFETII: str = '\U0001F38A'

player: str = ""
points: int


def main() -> None:
    """Houses the greeting, game loop, game functions, and game end."""
    greet()
    global points
    points = 0
    player_choice: int = 0
    while player_choice != 3:
        print(f"Input 1 to play the Face Slot Machine {PURPLE_FACE}{SUNGLASS_FACE}{HOT_FACE}")
        print(f"Input 2 to play the Animal Slot Machine {CHICK}{LION}{OCTOPUS}")
        player_choice = int(input(f"Input 3 to exit the game {DOOR}: "))
        if player_choice == 1:
            face_slot()

        if player_choice == 2:
            points = animal_slot(points)
        print(f"{MONEY_BAG}YOU HAVE {points} POINTS{MONEY_BAG}")

    print(f"{WAVING_HAND}{WAVING_HAND} Thank you for playing {player}! {WAVING_HAND}{WAVING_HAND}")
    print(f"{CONFETII}{CONFETII} You ended with {points} Points! {CONFETII}{CONFETII}")


def face_slot() -> None:
    """Slot Machine with face emojis- Custom Procedure."""
    global points
    slot1: str
    slot2: str
    slot3: str
    player_input: int = 0
    print(f"{HOT_FACE}{SUNGLASS_FACE}{PURPLE_FACE} Great choice {player}! Welcome to the Face Slot Machine {PURPLE_FACE}{SUNGLASS_FACE}{HOT_FACE}")
    while player_input != 2:
        player_input = int(input("Input 1 to spin, input 2 to leave: "))
        if player_input == 1:
            slot1 = choice([PURPLE_FACE, SUNGLASS_FACE, HOT_FACE])
            slot2 = choice([PURPLE_FACE, SUNGLASS_FACE, HOT_FACE])
            slot3 = choice([PURPLE_FACE, SUNGLASS_FACE, HOT_FACE])

            print(f"{SLOT_MACHINE} Face Slot Machine {SLOT_MACHINE}")
            print("****************")
            print(f"| {slot1} | {slot2} | {slot3} |")
            print("****************")
            if slot1 == slot2 and slot2 == slot3 and slot1 == slot3:
                print(f"{MONEY_BAG}{MONEY_FACE}JACKPOT {player}, YOU WIN 5000 POINTS{MONEY_FACE}{MONEY_BAG}")
                points = points + 5000
                print(f"{MONEY_BAG}YOU HAVE {points} POINTS{MONEY_BAG}")
            else:
                print(f"{SAD_FACE}Bummer!{SAD_FACE}")


def animal_slot(point_tracker: int) -> int:
    """Slot Machine with animal emojis- Custom Function."""
    slot1: str
    slot2: str
    slot3: str
    player_input: int = 0
    print(f"{OCTOPUS}{LION}{CHICK} Great choice {player}! Welcome to the Animal Slot Machine {CHICK}{LION}{OCTOPUS}")
    while player_input != 2:
        player_input = int(input("Input 1 to spin, input 2 to leave: "))
        if player_input == 1:
            slot1 = choice([CHICK, LION, OCTOPUS])
            slot2 = choice([CHICK, LION, OCTOPUS])
            slot3 = choice([CHICK, LION, OCTOPUS])

            print("{SLOT_MACHINE} Animal Slot Machine {SLOT_MACHINE}")
            print("****************")
            print(f"| {slot1} | {slot2} | {slot3} |")
            print("****************")
            if slot1 == slot2 and slot2 == slot3 and slot1 == slot3:
                print(f"{MONEY_BAG}{MONEY_FACE}JACKPOT {player}, YOU WIN 5000 POINTS{MONEY_FACE}{MONEY_BAG}")
                point_tracker = point_tracker + 5000
                print(f"{MONEY_BAG}YOU HAVE {point_tracker} POINTS{MONEY_BAG}")
            else:
                print(f"{SAD_FACE}Bummer!{SAD_FACE}")

    return point_tracker


def greet() -> None:
    """Greets player and sets name."""
    global player
    print(f"{SLOT_MACHINE} Come test your luck at the Spectacular Slot Machine Challenge! {SLOT_MACHINE}")
    print("In this game, you will try to win points by getting 3 emojis to match!")
    player = input("Please enter your player name to continue! ")


if __name__ == "__main__":
    main()
