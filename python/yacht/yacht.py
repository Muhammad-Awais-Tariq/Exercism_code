"""Scoring functions for the Yacht dice game."""

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
    """Calculate the score for a dice roll and category.

    ```
    Parameters:
        dice (list): Five dice values.
        category (int): The category to score.

    Returns:
        int: The score for the given dice and category.
    """
    
    if category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        return category * dice.count(category)

    if category == CHOICE:
        return sum(dice)

    if category == YACHT:
        return 50 if len(set(dice)) == 1 else 0

    value_counts = {}

    for die in dice:
        if die in value_counts:
            value_counts[die] += 1
        else:
            value_counts[die] = 1

    if category == FULL_HOUSE:
        counts = list(value_counts.values())

        if counts == [2, 3] or counts == [3, 2]:
            return sum(dice)

        return 0

    if category == FOUR_OF_A_KIND:
        for value, count in value_counts.items():
            if count >= 4:
                return value * 4

        return 0

    if category == LITTLE_STRAIGHT:
        return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0

    if category == BIG_STRAIGHT:
        return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0

    return 0
