import math


def score(x, y):
    """Calculate the score earned by a dart landing at the given coordinates.

    Parameters:
        x (float): The x-coordinate of the dart's landing position.
        y (float): The y-coordinate of the dart's landing position.

    Returns:
        int: The score earned based on the dart's distance from the center
        of the target.
    """

    distance = math.dist([0, 0], [x, y])

    if distance <= 1:
        return 10

    if distance <= 5:
        return 5

    if distance <= 10:
        return 1

    return 0