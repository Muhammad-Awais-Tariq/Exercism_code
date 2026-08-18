
ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"]

tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def two_digit(n):
    if n < 20:
        return ones[n]
    t, o = divmod(n, 10)
    return tens[t] + ("-" + ones[o] if o else "")

def say(number):
    """Convert a number into its alphabetic representation.

    Parameters:
        number (int): The number to be converted.

    Returns:
        str: The alphabetic representation of the number.
    """
