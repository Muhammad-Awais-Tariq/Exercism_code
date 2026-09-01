class Queen:
    """Represent a queen's position on an 8x8 chessboard."""

    def __init__(self, row, column):
        """Initialize a queen with a row and column position.

        Parameters:
            row (int): The row position of the queen.
            column (int): The column position of the queen.

        Raises:
            ValueError: If the row or column is negative or outside
                the chessboard.
        """

        if row < 0:
            raise ValueError("row not positive")

        if column < 0:
            raise ValueError("column not positive")

        if 0 > row or row > 7:
            raise ValueError("row not on board")

        if 0 > column or column > 7:
            raise ValueError("column not on board")

        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        """Determine whether this queen can attack another queen.

        Queens can attack each other when they are on the same row,
        column, or diagonal.

        Parameters:
            another_queen (Queen): The other queen to check against.

        Returns:
            bool: True if the queens can attack each other, otherwise False.

        Raises:
            ValueError: If both queens occupy the same square.
        """

        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        if self.column == another_queen.column or self.row == another_queen.row:
            return True

        if abs(self.row - another_queen.row) == abs(self.column - another_queen.column):
            return True

        return False