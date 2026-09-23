class Clock:
    """Represent a 24-hour clock."""

    def __init__(self, hour, minute):
        """Initialize the clock with the given hour and minute.

        Parameters:
            hour (int): The hour of the clock.
            minute (int): The minute of the clock.
        """
        total_minutes = hour * 60 + minute

        self.hour = (total_minutes // 60) % 24
        self.minute = total_minutes % 60

    def __repr__(self):
        """Return the official string representation of the clock.

        Returns:
            str: The clock representation in the format 'Clock(hour, minute)'.
        """
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        """Return the clock time in a human-readable format.

        Returns:
            str: The clock time in the format 'HH:MM'.
        """
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        """Compare this clock with another clock.

        Parameters:
            other (Clock): The clock to compare with.

        Returns:
            bool: True if both clocks represent the same time, otherwise False.
        """
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        """Return a new clock with minutes added.

        Parameters:
            minutes (int): The number of minutes to add.

        Returns:
            Clock: A new clock with the added minutes.
        """
        new_minutes = self.minute + minutes
        return Clock(self.hour, new_minutes)

    def __sub__(self, minutes):
        """Return a new clock with minutes subtracted.

        Parameters:
            minutes (int): The number of minutes to subtract.

        Returns:
            Clock: A new clock with the subtracted minutes.
        """
        new_minutes = self.minute - minutes
        return Clock(self.hour, new_minutes)