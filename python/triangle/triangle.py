
def check_valid_triangle(sides):
    """ Checks if the given sides are valid for triangle.

    Parameters:
        sides(List) : sides of the triangle.
    
    Returns:
        bool: True if the sides are valid else False.
    """

    for side in sides:
        if side <= 0:
            return False
    
    if sides[0] + sides[1] < sides[2]:
        return False
    elif sides[1] + sides[2] < sides[0]:
        return False
    elif sides[0] + sides[2] < sides[1]:
        return False

    return True


def equilateral(sides):
    """Checks if the triangle is equilateral.

    Parameters:
        sides(List) : sides of the triangle.

    Returns:
        bool: True if the sides are all equal else False.    
    
    """
    if not check_valid_triangle(sides):
        return False
    
    return len(set(sides)) == 1


def isosceles(sides):
    """Checks if the triangle is isosceles.

    Parameters:
        sides(List) : sides of the triangle.

    Returns:
        bool: True if two sides are all equal else False.    
    
    """    

    if not check_valid_triangle(sides):
        return False
    
    if equilateral(sides):
        return True
    
    return len(set(sides)) == 2


def scalene(sides):
    pass
