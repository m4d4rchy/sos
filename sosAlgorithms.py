#!/usr/bin/python3

def newBoard(n):
    board = [[0] * n for i in range(n)]
    return(board)

def possibleSquare(board, n, i, j):
    if ((i >= 0 and j >= 0) and (i <= n and j <= n) and board[i][j] == 0):
        return(True)
    else:
        return(False)

def updateScoreS(board, n, i, j, scores, player, lines):
    if (i == 0 and j == 0):
        if (board[i][j + 1] == 2 and board[i][j + 2] == 1):
            scores[player - 1] = scores[player - 1] + 1
            lines.extend([i, j, i, j + 2])
    elif (i == (n - 1) and j == (n - 1)):
    elif (i == 0):
    elif (i == (n - 1)):
    elif (j == 0):
    elif (j == (n - 1)):
    else:

def updateScoreO(board, n, i, j, scores, player, lines):
    if (i == 0 and j == 0):
        if (board[i][j + 1] == 2 and board[i][j + 2] == 1):
            scores[player - 1] = scores[player - 1] + 1
            lines.extend([i, j, i, j + 2])
    elif (i == (n - 1) and j == (n - 1)):
    elif (i == 0):
    elif (i == (n - 1)):
    elif (j == 0):
    elif (j == (n - 1)):
    else: