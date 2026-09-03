# Score categories.
# Change the values as you see fit.
YACHT = None
ONES = 1
TWOS = 2
THREES = 3
FOURS = None
FIVES = None
SIXES = None
FULL_HOUSE = None
FOUR_OF_A_KIND = None
LITTLE_STRAIGHT = None
BIG_STRAIGHT = None
CHOICE = None


def score(dice, category):
    """Returns the score based on the dice and category.

    Parameters:
        dice (list): The dice roll.
        category (int): The category on the basic of which we want calculation.
    
    Return:
        int: The total score.
    """

    if category == 1:
        return dice.count(1)

    if category == 2:
        return 2 * dice.count(2)

    if category == 3:
        return 3 * dice.count(3)