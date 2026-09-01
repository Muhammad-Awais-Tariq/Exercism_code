class Queen:
    def __init__(self, row, column):
        """Construtor to store the rows and coloumn of queen.

        Parameters:
            row(int): The row of the queen.
            coloumn (int): The column of the queen.
        """

        if row < 0:
            raise ValueError("row not positive")

        if column < 0:
            raise ValueError("column not positive")

        if 0 > row  or row > 7:
            raise ValueError("row not on board")

        if 0 > column  or column > 7:
            raise ValueError("column not on board")

        self.row = row
        self.column = column


    def can_attack(self, another_queen):
        pass
