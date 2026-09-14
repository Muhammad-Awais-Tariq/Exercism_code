class HighScores:
    """ Contains the high scores of the tests."""
    def __init__(self, scores):
        """Constructor of the scores.

        Parameters:
            scores (list): All the test scores.
        """

        self.scores = scores

    def latest(self):
        """Reutrn the latest scores.

        Returns:
            int: The latest score.
        """

        return self.scores[-1]

    def personal_best(self):
        """Return the personal best score.

        Returns:
            int : The best score
        
        """

        return max(self.scores)

    def personal_top_three(self):
        """Returns the top 3 scores.

        Returns:
            list : The top 3 scores.
        """