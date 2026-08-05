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


    def on_earth(self):
        """Calculate the person's age in Earth years.

        Returns:
            float: The person's age in Earth years.
        """

        return self._calculate_earth_age()


    def on_mercury(self):
        """Calculate the person's age in Mercury years.

        Returns:
            float: The person's age in Mercury years.
        """

        earth_age = self._calculate_earth_age()
        mercury_orbit = 0.2408467
        return earth_age / mercury_orbit


    def on_venus(self):
        """Calculate the person's age in Mercury years.

        Returns:
            float: The person's age in Mercury years.
        """        
        earth_age = self._calculate_earth_age()
        Venus_orbit = 0.61519726
        return earth_age / Venus_orbit    

    def on_mars(self):
        """Calculate the person's age in Mars years.

        Returns:
            float: The person's age in Mars years.
        """        

        earth_age = self._calculate_earth_age()
        Mars_orbit = 1.8808158
        return earth_age / Mars_orbit   

    def on_jupiter(self):
        """Calculate the person's age in Jupiter years.

        Returns:
            float: The person's age in Jupiter years.
        """      

        earth_age = self._calculate_earth_age()
        Jupiter_orbit = 11.862615
        return earth_age / Jupiter_orbit             
         
