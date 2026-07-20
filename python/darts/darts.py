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

    distance = math.dist(x , y)

    if distance <= 1:
        return 10
    
    if 1 < distance <= 5 :
        return 5
    
    if 5 < distance <= 10:
        return 1