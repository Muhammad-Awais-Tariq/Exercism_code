class Matrix:
    def __init__(self, matrix_string):
        self.final_row = []
        for row in matrix_string.split("\n"):
            current_row = []
            for element in row.split(" "):
                    current_row.append(int(element))
            self.final_row.append(current_row)
        
    def row(self, index):
        pass

    def column(self, index):
        pass
