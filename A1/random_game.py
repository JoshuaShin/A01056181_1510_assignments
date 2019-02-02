"""
random_game.py.

Play a game of rock paper scissors with the computer.
"""

# Joshua Shin
# A01056181
# Jan 25 2019

import doctest
import random


def choice_computer_translator(choice_computer):
    """
    Translate computer choice (int between 0 - 2 inclusive) to "rock", "paper", or "scissors".
    PARAM choice_computer int between 0 - 2
    PRE-CONDITION choice_computer must be int between 0 - 2
    POST-CONDITION translate computer choice to "rock", "paper", or "scissors"
    RETURN return computer choice in "rock", "paper", or "scissors"

    >>> choice_computer_translator(0)
    'rock'
    >>> choice_computer_translator(1)
    'paper'
    >>> choice_computer_translator(2)
    'scissors'
    """

    if choice_computer == 0:
        return "rock"

    elif choice_computer == 1:
        return "paper"

    else:  # choice_computer == 2
        return "scissors"


def rock_paper_scissors():
    """
    Play a game of rock paper scissors with the computer.
    """

    choice_computer = choice_computer_translator(random.randint(0, 2))
    choice_player = input("Ready? Rock, paper, scissors!: ").strip().lower()

    if not(choice_player == "rock" or choice_player == "paper" or choice_player == "scissors"):
        print("Dont you know how to play rock paper scissors, ya loser!")
        rock_paper_scissors()
        return

    print("Computer played:", choice_computer)
    print("You played:", choice_player)

    if choice_player == choice_computer:
        print("TIED")

    elif choice_player == "rock":
        if choice_computer == "paper":
            print("YOU LOSE")
        elif choice_computer == "scissors":
            print("YOU WIN")

    elif choice_player == "paper":
        if choice_computer == "scissors":
            print("YOU LOSE")
        elif choice_computer == "rock":
            print("YOU WIN")

    elif choice_player == "scissors":
        if choice_computer == "rock":
            print("YOU LOSE")
        elif choice_computer == "paper":
            print("YOU WIN")


def main():
    """
    Drive the program.
    """

    doctest.testmod()
    rock_paper_scissors()


if __name__ == "__main__":
    main()
