class Allergies:

    def __init__(self, score):
        """Stores the score.

        Parameters:
            scores (int): The score that we need.
        """

        self.score = score
        self.mapping = {
            "eggs": 1,
            "peanuts": 2,
            "shellfish": 4,
            "strawberries": 8,
            "tomatoes": 16,
            "chocolate": 32,
            "pollen": 64,
            "cats": 128,
        }

    def allergic_to(self, item):
        """Checks if the value is present of item or not.

        Parameters:
            item (str): The item that we are checking.
        """

        if self.score & self.mapping[item] == self.mapping[item]:
            return True
        else:
            return False

    @property
    def lst(self):
        """returns the list of all the alergies."""
