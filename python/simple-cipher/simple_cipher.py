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

        shift = ord(self.key) - ord("a")

        new_txt = ""

        for char in text:
            new_char = (ord(char) - ord("a") + shift) % 26
            new_txt += chr(new_char + ord("a"))

        return new_txt

    def decode(self, text):
        pass
