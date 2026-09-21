import string
import math

def cipher_text(plain_text):
    """Cipher the text from the plain to the ciphered.

    Parameters:
        plain_text (str): The plain text to be ciphered.
    
    Returns:
        str: The chipered text.
    """

    
    clean_text = plain_text.translate(str.maketrans('', '', string.punctuation))
    clean_text = clean_text.replace(" " , "").lower()

    if not clean_text:
        return ""
    
    columns = math.ceil(math.sqrt(len(clean_text)))

    rows = math.ceil(len(clean_text) / columns)

    result = ""

    for i in range(columns):
        for j in range(rows):
            index = j * columns + i
            try:
                result += clean_text[index]
            except IndexError:
                result += " "
                
        if i < columns - 1:
            result += " "

    return result