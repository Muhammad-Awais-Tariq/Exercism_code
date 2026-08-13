def encode(plain_text):
    """Encode plain text using the Atbash cipher.

    Parameters:
        plain_text (str): The plain text to encode.

    Returns:
        str: The encoded text.
    """

    output_str = ""

    for char in plain_text:
        ascii_char = ord(char)
        position = (ascii_char - 97) + 1
        new_position = (27 - position) + 97
        output_str += chr(new_position)

def decode(ciphered_text):
    pass
