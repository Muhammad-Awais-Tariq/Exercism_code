EAST = 1
NORTH = 0
WEST = 3
SOUTH = 2


class Robot:
    """Represent a robot that can move around a grid."""

    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        """Initialize the robot with a direction and coordinates.

        Parameters:
            direction (int): The robot's starting direction.
            x_pos (int): The robot's starting x-coordinate.
            y_pos (int): The robot's starting y-coordinate.
        """
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, moves):
        """Move the robot according to the given instructions.

        Parameters:
            moves (str): A string containing the movement instructions.
        """
        for move in moves:
            if move == "R":
                if self.direction != 3:
                    self.direction += 1
                else:
                    self.direction = 0

            if move == "L":
                if self.direction != 0:
                    self.direction -= 1
                else:
                    self.direction = 3

            if move == "A":
                x, y = self.coordinates

                if self.direction == 0:
                    self.coordinates = (x, y + 1)
                elif self.direction == 1:
                    self.coordinates = (x + 1, y)
                elif self.direction == 2:
                    self.coordinates = (x, y - 1)
                else:
                    self.coordinates = (x - 1, y)