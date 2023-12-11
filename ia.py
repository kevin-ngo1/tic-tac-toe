import random

def ia_difficile(board, signe):
    for i in range(3):
        if board[i][0] == board[i][1] == signe and board[i][2] == 0:
            return i * 3 + 2
        elif board[i][0] == board[i][2] == signe and board[i][1] == 0:
            return i * 3 + 1
        elif board[i][1] == board[i][2] == signe and board[i][0] == 0:
            return i * 3

        if board[0][i] == board[1][i] == signe and board[2][i] == 0:
            return 6 + i
        elif board[0][i] == board[2][i] == signe and board[1][i] == 0:
            return 3 + i
        elif board[1][i] == board[2][i] == signe and board[0][i] == 0:
            return i

    if board[0][0] == board[1][1] == signe and board[2][2] == 0:
        return 8
    elif board[0][0] == board[2][2] == signe and board[1][1] == 0:
        return 4
    elif board[1][1] == board[2][2] == signe and board[0][0] == 0:
        return 0
    elif board[0][2] == board[1][1] == signe and board[2][0] == 0:
        return 6
    elif board[0][2] == board[2][0] == signe and board[1][1] == 0:
        return 4
    elif board[1][1] == board[2][0] == signe and board[0][2] == 0:
        return 2

    available_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                available_moves.append(i * 3 + j)
    if available_moves:
        return random.choice(available_moves)

    return False

def ia_facile(board, signe):
    available_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                available_moves.append(i * 3 + j)
    if available_moves:
        return random.choice(available_moves)
    return False


