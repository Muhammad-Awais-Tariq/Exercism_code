class Matrix:
    def __init__(self, matrix_string):
        self.final_row = []
        for row in matrix_string.split("\n"):
            current_row = []
            for element in row.split(" "):
                    current_row.append(int(element))
            self.final_row.append(current_row)
        
    def row(self, index):
        """Return the row of the matrix based on the index.

        Parameters:
            index (int): The row index that we want.
        
        Return:
            list: The row based on the index.
        """

        return self.final_row[index-1]

    def column(self, index):
        pass
