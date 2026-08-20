def decode(string):
    """Decode a run-length encoded string.

    Parameters:
        string (str): The string to decode.

    Returns:
        str: The decoded string.
    """

    result = ""
    i = 0

    while i < len(string):
        count = ""

        while i < len(string) and string[i].isdigit():
            count += string[i]
            i += 1

        if count:
            count = int(count)
        else:
            count = 1

        result += string[i] * count
        i += 1

    return result


def encode(string):
    """Encode a string using run-length encoding.

    Parameters:
        string (str): The string to encode.

    Returns:
        str: The run-length encoded string.
    """

    result = ""
    i = 0
    while i < len(string):
        count = 1
        while i + 1 < len(string) and string[i] == string[i+1]:
            count += 1
            i += 1
        if count != 1:
            result += f"{count}{string[i]}"
        else:
            result += f"{string[i]}"
        i+= 1

    return result