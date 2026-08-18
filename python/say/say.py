
ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"]

tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def two_digit(n):
    if n < 20:
        return ones[n]
    t, o = divmod(n, 10)
    return tens[t] + ("-" + ones[o] if o else "")

def three_digit(n):
    if n < 100:
        return two_digit(n)
    h, rem = divmod(n, 100)
    result = ones[h] + " hundred"
    if rem:
        result += " " + two_digit(rem)
    return result

def say(number):
    """Convert a number into its alphabetic representation.

    Parameters:
        number (int): The number to be converted.

    Returns:
        str: The alphabetic representation of the number.
    """
    if n == 0:
        return "zero"

    billions, n = divmod(n, 1_000_000_000)
    millions, n = divmod(n, 1_000_000)
    thousands, n = divmod(n, 1_000)
    rest = n

    words = ""
    if billions:
        words += three_digit(billions) + " billion "
    if millions:
        words += three_digit(millions) + " million "
    if thousands:
        words += three_digit(thousands) + " thousand "
    if rest:
        words += three_digit(rest)

    return words.strip()
