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

    def move(self , moves):
        """Moves the robot based on the given moves.

        Parameters:
            moves(str) : The string containing all the moves.
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
                x , y = self.coordinates
                if self.direction == 0:
                    self.coordinates = (x,y+1)        
                elif self.direction == 1:
                    self.coordinates = (x+1,y)    
                elif self.direction == 2:
                    self.coordinates = (x,y-1)   
                else:
                    self.coordinates = (x-1,y)    

