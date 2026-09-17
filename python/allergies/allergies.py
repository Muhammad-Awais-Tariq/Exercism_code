class Allergies:
    """Represent a person's allergy score and allergies."""

    def __init__(self, score):
        """Initialize the allergy score.

        Parameters:
            score (int): The person's allergy score.
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
        """Check whether the person is allergic to an item.

        Parameters:
            item (str): The allergy item to check.

        Returns:
            bool: True if the person is allergic to the item,
                otherwise False.
        """

        return self.score & self.mapping[item] == self.mapping[item]

    @property
    def lst(self):
        """Return a list of all allergies."""

        current_allergies = []

        for item in self.mapping:
            if self.score & self.mapping[item] == self.mapping[item]:
                current_allergies.append(item)

        return current_allergies