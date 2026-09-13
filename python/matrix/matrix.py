class Matrix:
    """Represent a matrix of integers."""

    def __init__(self, matrix_string):
        """Initialize the matrix from a string representation.

        Parameters:
            matrix_string (str): A string containing rows of space-separated
                integers, with rows separated by newlines.
        """
        self.rows = []

        for row in matrix_string.split("\n"):
            current_row = []

            for element in row.split(" "):
                current_row.append(int(element))

            self.rows.append(current_row)

    def row(self, index):
        """Return a row from the matrix.

        Parameters:
            index (int): The 1-based index of the requested row.

        Returns:
            list: The requested row of integers.
        """
        return self.rows[index - 1]

    def column(self, index):
        """Return a column from the matrix.

        Parameters:
            index (int): The 1-based index of the requested column.

        Returns:
            list: The requested column of integers.
        """
        required_column = []

        for row in self.rows:
            required_column.append(row[index - 1])

        return required_column