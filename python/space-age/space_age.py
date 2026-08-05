class SpaceAge:
    """Represent a person's age in seconds.

    Store an age in seconds and provide methods to calculate
    the equivalent age on each planet.
    """

    def __init__(self, seconds):
        self.seconds = seconds

    def _calculate_earth_age(self):
        earth_year_in_seconds = 31557600
        return self.seconds / earth_year_in_seconds
