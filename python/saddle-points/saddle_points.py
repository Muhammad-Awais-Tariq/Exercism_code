def saddle_points(matrix):
    """Find all saddle points in a matrix.

    ```
    Parameters:
        matrix (list): The matrix to search for saddle points.

    Returns:
        list: A list of dictionaries containing the row and column
            positions of all saddle points.

    Raises:
        ValueError: If the matrix has rows of different lengths.
    """

    answer = []

    if not matrix:
        return answer

    first_row_length = len(matrix[0])

    for row_index in range(1, len(matrix)):
        if len(matrix[row_index]) != first_row_length:
            raise ValueError("irregular matrix")

    for row_index, row_values in enumerate(matrix):
        row_max = max(row_values)

        max_columns = [
            column_index
            for column_index, value in enumerate(row_values)
            if value == row_max
        ]

        for max_column in max_columns:
            for row in range(len(matrix)):
                if matrix[row][max_column] < row_max:
                    break
            else:
                answer.append(
                    {"row": row_index + 1, "column": max_column + 1}
                )

    return answer