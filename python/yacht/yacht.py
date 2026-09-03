# Score categories.
# Change the values as you see fit.
YACHT = None
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
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

    if category in [1 ,2 ,3 ,4 ,5 ,6]:
        return category * dice.count(category)