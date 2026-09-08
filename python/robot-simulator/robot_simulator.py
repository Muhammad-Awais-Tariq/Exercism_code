EAST = 1
NORTH = 0
WEST = 3
SOUTH = 2


class Robot:
    """
    A robot class to handle the robot movements.
    """
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        """Construtor for intilization.

        Parameters:
            direction: The start direction.
            x_pos : The x position.
            y_post: The y position
        """

        self.direction = direction
        self.coordinates = (x_pos , y_pos)

    
