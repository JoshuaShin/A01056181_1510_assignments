"""
colour_mixer.py

Print secondary color from two primary color inputs.
"""

# Joshua Shin
# A01056181
# Jan 24 2019


def color_mixer():
    """
    Print secondary color from two primary color inputs.
    """

    color = ["color_1", "color_2"]
    primary_color = ["red", "yellow", "blue"]

    color[0] = input("First primary color: ").strip().lower()
    if not(color[0] in primary_color):
        print("Please input a primary color!")
        color_mixer()
        return

    color[1] = input("Second primary color: ").strip().lower()
    if not(color[1] in primary_color):
        print("Please input a primary color!")
        color_mixer()
        return

    if color[0] == color[1]:
        print("First and second colors must be different!")
        color_mixer()

    if "red" in color and "blue" in color:
        print("Secondary color: purple")

    elif "red" in color and "yellow" in color:
        print("Secondary color: orange")

    elif "yellow" in color and "blue" in color:
        print("Secondary color: green")


def main():
    """
    Drive the program.
    """

    color_mixer()


if __name__ == "__main__":
    main()
