import string


def encode(plain_text):
    """Encode plain text using the Atbash cipher.

    Parameters:
        plain_text (str): The plain text to encode.

    Returns:
        str: The encoded text.
    """

    output_str = ""

    for char in plain_text:
        if char.isalpha():
            lowercase_char = char.lower()
            ascii_char = ord(lowercase_char)
            position = ascii_char - 97
            new_position = (25 - position) + 97
            output_str += chr(new_position)

        elif char not in string.punctuation and char not in string.whitespace:
            output_str += char

    final_string = []

    for index in range(0, len(output_str), 5):
        final_string.append(output_str[index:index + 5])

    return " ".join(final_string)


def decode(ciphered_text):
    """Decode ciphered text using the Atbash cipher.

    Parameters:
        ciphered_text (str): The ciphered text to decode.

    Returns:
        str: The decoded text.
    """

    output_str = ""

    for char in ciphered_text:
        if char.isalpha():
            lowercase_char = char.lower()
            ascii_char = ord(lowercase_char)
            position = ascii_char - 97
            new_position = (25 - position) + 97
            output_str += chr(new_position)

        elif char not in string.punctuation and char not in string.whitespace:
            output_str += char

    return output_str