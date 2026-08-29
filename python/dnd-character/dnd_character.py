import random

class Character:
    def __init__(self):
        """Initializes the character's abilities and hitpoints.
        """

        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        """Randomly generates an ability score.

        Returns:
            int: The character's ability score.
        """

        values = []

        for _ in range(4):
            values.append(random.randint(1 , 6))

        values = sorted(values)

        return sum(values[1:])
    
def modifier(value):
    """Modifies the given value.

    Parameters:
        value (int): The value to be modified.

    Returns:
        int: The modified value.
    """

    return (value - 10 ) // 2
