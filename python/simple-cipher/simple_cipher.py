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

    def decode(self, text):
        pass
