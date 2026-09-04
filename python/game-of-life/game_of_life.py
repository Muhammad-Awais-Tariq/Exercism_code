def tick(matrix):
    """Generate the next generation of Conway's Game of Life.

    Parameters:
        matrix (list): A 2D matrix representing the current generation,
            where 1 represents a live cell and 0 represents a dead cell.

    Returns:
        list: A 2D matrix representing the next generation.
    """
    
    if not matrix:
        return []

    new_matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    count = 0

    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if row - 1 >= 0 and matrix[row - 1][column] == 1:
                count += 1

            if row + 1 < len(matrix) and matrix[row + 1][column] == 1:
                count += 1

            if column - 1 >= 0 and matrix[row][column - 1] == 1:
                count += 1

            if column + 1 < len(matrix[0]) and matrix[row][column + 1] == 1:
                count += 1

            if (
                row - 1 >= 0
                and column - 1 >= 0
                and matrix[row - 1][column - 1] == 1
            ):
                count += 1

            if (
                row - 1 >= 0
                and column + 1 < len(matrix[0])
                and matrix[row - 1][column + 1] == 1
            ):
                count += 1

            if (
                row + 1 < len(matrix)
                and column - 1 >= 0
                and matrix[row + 1][column - 1] == 1
            ):
                count += 1

            if (
                row + 1 < len(matrix)
                and column + 1 < len(matrix[0])
                and matrix[row + 1][column + 1] == 1
            ):
                count += 1

            if matrix[row][column] == 1 and count in (2, 3):
                new_matrix[row][column] = 1

            if matrix[row][column] == 0 and count == 3:
                new_matrix[row][column] = 1

            count = 0

    return new_matrix