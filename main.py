import random


def sum(a, b, c):
    """Calculate the sum of three values.

    Parameters:
        a (int): First value.
        b (int): Second value.
        c (int): Third value.

    Returns:
        int: The sum of the three values.
    """
    return a + b + c


def printBoard(xState, zState):
    """Print the Tic Tac Toe game board.

    Parameters:
        xState (list): Current state of X player's moves (1 for occupied, 0 for empty).
        zState (list): Current state of O player's moves (1 for occupied, 0 for empty).

    Returns:
        None
    """
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")


def checkWin(xState, zState):
    """Check if there's a winner in the current game board.

    Parameters:
        xState (list): Current state of X player's moves (1 for occupied, 0 for empty).
        zState (list): Current state of O player's moves (1 for occupied, 0 for empty).

    Returns:
        int: 1 if X player wins, 0 if O player wins, -1 if no winner yet.
    """
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
            [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if (sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            return 1
        if (sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            return 0
    return -1


def checkDraw(xState, zState):
    """Check if the game is a draw (no winner and the board is full).

    Parameters:
        xState (list): Current state of X player's moves (1 for occupied, 0 for empty).
        zState (list): Current state of O player's moves (1 for occupied, 0 for empty).

    Returns:
        bool: True if the game is a draw, False otherwise.
    """
    return checkWin(xState, zState) == -1 and all(xState[i] or zState[i] for i in range(9))


def get_ai_move(xState, zState):
    """Get the AI player's move using the Minimax algorithm.

    Parameters:
        xState (list): Current state of X player's moves (1 for occupied, 0 for empty).
        zState (list): Current state of O player's moves (1 for occupied, 0 for empty).

    Returns:
        int: Index of the selected move for the AI player.
    """
    available_moves = [i for i, val in enumerate(
        xState) if val == 0 and zState[i] == 0]

    best_move = -1
    best_score = float('-inf')  # Initialize to negative infinity

    for move in available_moves:
        zState[move] = 1
        score = minimax(xState, zState, False)
        zState[move] = 0  # Reset the move

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def minimax(xState, zState, is_maximizing):
    """Minimax algorithm to evaluate the best move for the AI player.

    Parameters:
        xState (list): Current state of X player's moves (1 for occupied, 0 for empty).
        zState (list): Current state of O player's moves (1 for occupied, 0 for empty).
        is_maximizing (bool): True for AI player's turn, False for Player's turn.

    Returns:
        int: The score of the best move for the current player.
    """
    winner = checkWin(xState, zState)
    if winner != -1:
        # AI's move gets higher score (1), Player's move gets lower score (-1)
        return 1 - 2*is_maximizing

    if checkDraw(xState, zState):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for move in range(9):
            if xState[move] == 0 and zState[move] == 0:
                zState[move] = 1
                score = minimax(xState, zState, False)
                zState[move] = 0
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for move in range(9):
            if xState[move] == 0 and zState[move] == 0:
                xState[move] = 1
                score = minimax(xState, zState, True)
                xState[move] = 0
                best_score = min(best_score, score)
        return best_score


if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe")

    while True:
        printBoard(xState, zState)

        if turn == 1:  # Player X's turn (Human player)
            print("X's Chance")
            value = int(input("Please enter a value: "))
            if xState[value] == 0 and zState[value] == 0:
                xState[value] = 1
            else:
                print("Invalid move. Try again.")
                continue
        else:  # Player O's turn (AI player)
            print("O's Chance")
            value = get_ai_move(xState, zState)
            zState[value] = 1
            print(f"Computer selected position: {value}")

        # Check if there's a winner or draw
        cwin = checkWin(xState, zState)
        if cwin == 1:
            print("X Won the match")
            break
        elif cwin == 0:
            print("O Won the match")
            break
        elif checkDraw(xState, zState):
            print("It's a draw")
            break

        turn = 1 - turn
