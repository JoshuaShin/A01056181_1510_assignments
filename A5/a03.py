"""
q03.py

Back up a given file with the same content and name with the extension .bak.
"""


# Joshua Shin
# A01056181
# April 15th 2019


def backup(file_name: str) -> None:
    """
    Back up a given file with the same content and name with the extension .bak.

    PRE-CONDITION file_name must be a valid file name
    POST-CONDITION back up with the same content is created, with the extension .bak
    """
    try:
        with open(file_name, 'r') as file_object:
            content = file_object.read()
            with open(file_name.split(".")[0] + ".bak", 'w') as file_object_new:
                file_object_new.write(content)
    except FileNotFoundError:
        print("The file does not exist.")


def main():
    backup("file.txt")


if __name__ == '__main__':
    main()
