def slices(series, length):
    """Return all consecutive slices of the given length from the series.

    Parameters:
        series (str): The series to create slices from.
        length (int): The length of each slice.

    Returns:
        list: A list containing the consecutive slices.
    """

    if not series:
        raise ValueError("series cannot be empty")
    
    if length == 0:
        raise ValueError("slice length cannot be zero")

    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    if length < 0:
        raise ValueError("slice length cannot be negative")

    final_elment = []

    for element in range(len(series) - length + 1):
        final_elment.append(series[element:element+length])

    return final_elment