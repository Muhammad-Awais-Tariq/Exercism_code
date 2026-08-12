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
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    """Determine the relationship between two lists.

    Parameters:
        list_one (list): The first list to compare.
        list_two (list): The second list to compare.

    Returns:
        str: The relationship between the lists: EQUAL, SUBLIST,
            SUPERLIST, or UNEQUAL.
    """

    size_a = len(list_one)
    size_b = len(list_two)

    if not list_one and not list_two:
        return EQUAL

    if list_one == list_two:
        return EQUAL

    if not list_one and list_two:
        return SUBLIST

    if list_one and not list_two:
        return SUPERLIST

    for i in range(size_b):
        partial_list = list_two[i:i+size_a]

        if len(partial_list) == size_a:
            if list_one == partial_list:
                return SUBLIST

    for i in range(size_a):
        partial_list = list_one[i:i+size_b]

        if len(partial_list) == size_b:
            if list_two == partial_list:
                return SUPERLIST

    return UNEQUAL
        