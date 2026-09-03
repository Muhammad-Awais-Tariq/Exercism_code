
YACHT = 7
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 0


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

    if category == 0:
        return sum(dice)

    if len(set(dice)) == 1:
        return 50
    
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

    if sorted(dice) == [2, 3, 4, 5, 6]:
        return 30

    return 0