
def find_factor(number):
    """Return the factors of a given number, excluding the number itself.

    Parameters:
        number (int): The number whose factors are to be found.

    Returns:
        list: The factors of the given number, excluding the number itself.
    """


def classify(number):
    """Classify a positive integer based on its aliquot sum.

    Parameters:
        number (int): A positive integer to classify.

    Returns:
        str: "perfect" if the aliquot sum equals the number,
            "abundant" if it is greater, or "deficient" if it is less.
    """
    
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    

