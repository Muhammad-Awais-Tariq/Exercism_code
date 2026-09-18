import string
import random

class Cipher:
    def __init__(self, key=None):
        """Constructor for the object intialization.

        Parameters:
            key(str): The based on which we will generate the text.
        """

        if key is None:
            self.key = "".join(random.choices(string.ascii_lowercase , k=100))
        else:
            self.key = key

    def encode(self, text):
        """Encode the text based on the key provided by the user.

        Parameters:
            text (str): The text that we want to encode
        """
        
        new_text = ""

        for index, char in enumerate(text):
            key_char = self.key[index % len(self.key)]

            shift = ord(key_char) - ord("a")
            new_char = (ord(char) - ord("a") + shift) % 26

            new_text += chr(new_char + ord("a"))

        return new_text


    def decode(self, text):
        pass
