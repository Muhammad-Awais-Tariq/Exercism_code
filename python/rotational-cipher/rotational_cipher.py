def rotate(text, key):
    """Return the text encrypted using a Caesar cipher.

    Parameters:
        text (str): The text to encrypt.
        key (int): The rotation key used for encryption.

    Returns:
        str: The encrypted text.
    """
    ciphered_text = ""

    for char in text:
        if char.isalpha():
            new_value_char = ord(char) + key
            if char.islower():
                if new_value_char > 122:
                    new_value_char -= 26
            else:
                if new_value_char > 90:
                    new_value_char -= 26                
            new_char = chr(new_value_char)
            ciphered_text += new_char
        else:
            ciphered_text += char

    return ciphered_text