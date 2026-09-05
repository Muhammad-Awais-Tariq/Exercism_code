def gamestate(board):
    """Determine the current state of a Tic-Tac-Toe game.

    Parameters:
        board (list): A 3x3 Tic-Tac-Toe board.

    Returns:
        str: The game state: "win", "draw", or "ongoing".

    Raises:
        ValueError: If the board has an invalid turn order or
            both players have won.
    """
    
    x_count = 0
    o_count = 0
    x_won = 0
    o_won = 0

    for row in board:
        for char in row:
            if char == "X":
                x_count += 1
            elif char == "O":
                o_count += 1

    if x_count < o_count and o_count >= 1:
        raise ValueError("Wrong turn order: O started")

    if x_count >= o_count + 2:
        raise ValueError("Wrong turn order: X went twice")

    if o_count > x_count:
        raise ValueError("Wrong turn order: O went twice")

    for i in range(3):
        if board[i][0] == " ":
            continue

        current_char = board[i][0]
        count = 1

        for j in range(1, 3):
            if board[i][j] == current_char:
                count += 1
            else:
                break

        if count == 3:
            if current_char == "X":
                x_won += 1
            else:
                o_won += 1

    for i in range(3):
        if board[0][i] == " ":
            continue

        current_char = board[0][i]
        count = 1

        for j in range(1, 3):
            if board[j][i] == current_char:
                count += 1
            else:
                break

        if count == 3:
            if current_char == "X":
                x_won += 1
            else:
                o_won += 1

    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "X":
            x_won += 1
        else:
            o_won += 1

    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "X":
            x_won += 1
        else:
            o_won += 1

    if x_won >= 1 and o_won >= 1:
        raise ValueError(
            "Impossible board: game should have ended after the game was won"
        )

    if x_won >= 1 or o_won >= 1:
        return "win"

    if x_count + o_count == 9:
        return "draw"

    return "ongoing"