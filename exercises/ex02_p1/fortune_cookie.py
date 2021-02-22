"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730237266"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2: Print the result of calling your fortune_cookie function.
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.
def fortune_cookie() -> str:
    """Tells the user a random fortune."""
    num: int = randint(1, 4)
    if num == 1:
        return "You will get an A in COMP110:)"
    else:
        if num == 2:
            return "You will get a new job this summer!"
        else:
            if num == 3:
                return "You will go on your dream vacation soon!"
            else:
                return "You will become a master coder :)"


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()