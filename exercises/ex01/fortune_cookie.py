"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730237266"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
num: int = randint(1, 4)
if num == 1:
    print("You will get an A in COMP110:)")
else:
    if num == 2:
        print("You will get a new job this summer!")
    else:
        if num == 3:
            print("You will go on your dream vacation soon!")
        else:
            print("You will become a master coder :)")
print("Now, go spread positive vibes!")