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