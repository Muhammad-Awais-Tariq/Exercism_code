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
            position = (ascii_char - 97) + 1
            new_position = (27 - position) + 97
            if char.isupper():
                output_str += chr(new_position).upper()
            else:
                output_str += chr(new_position)    
        else:        
            output_str += char

    return output_str

def decode(ciphered_text):
    pass
