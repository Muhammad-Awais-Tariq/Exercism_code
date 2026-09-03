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

    value_counts = {}

    for die in dice:
        if die in value_counts:
            value_counts[die] += 1
        else:
            value_counts[die] = 1

    if list(value_counts.values()) == [2 ,3] or list(value_counts.values()) == [3 , 2]:
        return sum(dice)

    for key , value in value_counts.items():
        if value >= 4:
            return key * 4

    if sorted(dice) == [1,2,3,4,5]:
        return 30