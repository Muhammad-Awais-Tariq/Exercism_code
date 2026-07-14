def leap_year(year):
    """ Determine whether the given year is leap year or not.
    
    Parameters:
        year(int) : The given year.
    
    Returns:
        bool: True if the year is a leap year, otherwise False.
    """
    
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    
    return False
