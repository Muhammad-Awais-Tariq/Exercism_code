"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = None
SUPERLIST = None
EQUAL = None
UNEQUAL = None


def sublist(list_one, list_two):
    """Determine the relationship between two lists.

    Parameters:
        list_one (list): The first list to compare.
        list_two (list): The second list to compare.

    Returns:
        str: The relationship between the lists: EQUAL, SUBLIST,
            SUPERLIST, or UNEQUAL.
    """
