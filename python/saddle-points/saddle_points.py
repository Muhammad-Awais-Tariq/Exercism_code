def saddle_points(matrix):
    """give the saddle points based on the matrix.

    Paramters:
        matrix (list): The matrix to find the positions.
    
    Return:
        list: The found saddle points
    """

    answer = []
    if not matrix:
        return answer

    first_row_len = len(matrix[0])
    for idx in range(1,len(matrix)):
        if len(matrix[idx]) != first_row_len:
            raise ValueError("irregular matrix")
        
    for i , rows in enumerate(matrix):
        row_max = max(rows)

        max_idx = [index for index , value in enumerate(rows) if value == row_max]

        for max_col in max_idx:
            for row in range(len(matrix)):
                if matrix[row][max_col] < row_max:
                    break
            else:     
                answer.append({"row": i+1, "column": max_col+1})

    return answer