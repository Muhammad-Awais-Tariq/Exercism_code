class HighScores:
    """Manage a player's high scores."""

    def __init__(self, scores):
        """Initialize a HighScores object with the given scores.

        Parameters:
            scores (list): The player's list of scores.
        """

        self.scores = scores

    def latest(self):
        """Return the player's latest score.

        Returns:
            int: The latest score in the list.
        """

        return self.scores[-1]

    def personal_best(self):
        """Return the player's highest score.

        Returns:
            int: The highest score in the list.
        """

        return max(self.scores)

    def personal_top_three(self):
        """Return the player's three highest scores.

        Returns:
            list: The three highest scores, ordered from highest to lowest.
        """
        
        return sorted(self.scores, reverse=True)[:3]