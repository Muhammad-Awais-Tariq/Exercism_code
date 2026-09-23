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

        self.hour = hour
        self.minute = minute

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

    def __eq__(self, other):
        pass

    def __add__(self, minutes):
        pass

    def __sub__(self, minutes):
        pass
