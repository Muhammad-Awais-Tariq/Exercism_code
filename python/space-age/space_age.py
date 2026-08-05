class SpaceAge:
    """Represent a person's age in seconds.

    Store an age in seconds and provide methods to calculate
    the equivalent age on each planet.
    """

    EARTH_YEAR_IN_SECONDS = 31557600


    def __init__(self, seconds):
        self.seconds = seconds


    def _calculate_earth_age(self):
        return self.seconds / self.EARTH_YEAR_IN_SECONDS


    def on_earth(self):
        """Calculate the person's age in Earth years.

        Returns:
            float: The person's age in Earth years.
        """
        return float(f"{self._calculate_earth_age():.2f}")


    def on_mercury(self):
        """Calculate the person's age in Mercury years.

        Returns:
            float: The person's age in Mercury years.
        """
        earth_age = self._calculate_earth_age()
        mercury_orbit = 0.2408467
        return float(f"{earth_age / mercury_orbit:.2f}")


    def on_venus(self):
        """Calculate the person's age in Venus years.

        Returns:
            float: The person's age in Venus years.
        """
        earth_age = self._calculate_earth_age()
        venus_orbit = 0.61519726
        return float(f"{earth_age / venus_orbit:.2f}")


    def on_mars(self):
        """Calculate the person's age in Mars years.

        Returns:
            float: The person's age in Mars years.
        """
        earth_age = self._calculate_earth_age()
        mars_orbit = 1.8808158
        return float(f"{earth_age / mars_orbit:.2f}")


    def on_jupiter(self):
        """Calculate the person's age in Jupiter years.

        Returns:
            float: The person's age in Jupiter years.
        """
        earth_age = self._calculate_earth_age()
        jupiter_orbit = 11.862615
        return float(f"{earth_age / jupiter_orbit:.2f}")


    def on_saturn(self):
        """Calculate the person's age in Saturn years.

        Returns:
            float: The person's age in Saturn years.
        """
        earth_age = self._calculate_earth_age()
        saturn_orbit = 29.447498
        return float(f"{earth_age / saturn_orbit:.2f}")


    def on_uranus(self):
        """Calculate the person's age in Uranus years.

        Returns:
            float: The person's age in Uranus years.
        """
        earth_age = self._calculate_earth_age()
        uranus_orbit = 84.016846
        return float(f"{earth_age / uranus_orbit:.2f}")


    def on_neptune(self):
        """Calculate the person's age in Neptune years.

        Returns:
            float: The person's age in Neptune years.
        """
        earth_age = self._calculate_earth_age()
        neptune_orbit = 164.79132
        return float(f"{earth_age / neptune_orbit:.2f}")