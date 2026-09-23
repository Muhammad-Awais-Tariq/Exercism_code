class Clock:
    """
    A clock class for handling all the clock related functionality.
    """
    def __init__(self, hour, minute):
        """Construtor to intialize hours and minutes.

        Parameters:
            hour (int): The hours of the time.
            minute (int): The minutes on the clock.
        """

        total_minutes = hour * 60 + minute
        self.hour = (total_minutes // 60 ) % 24
        self.minute = total_minutes % 60

    def __repr__(self):
        """Returns the representation of the class.

        Returns:
            str: The object of the class.
        """

        return f"Clock({self.hour}, {self.minute})"
    
    def __str__(self):
        """Gives the string representation of class.

        Returns:
            str: The str representation of the object.

        """

        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        pass

    def __add__(self, minutes):
        pass

    def __sub__(self, minutes):
        pass
