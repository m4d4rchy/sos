#!/usr/bin/python3

def newBoard(n):
    board = [[0] * n for i in range(n)]
    return(board)

def possibleSquare(board, n, i, j):
        if (board[i][j] == 0):
                return(True)
        else:
                return(False)

def updateScoreS(board, n, i, j, scores, player):
        lines = [[]]
        if (i == 0 and j == 0):
                if (board[i][j] == 1 and board[i][j + 1] == 2 and board[i][j + 2] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i, j, i, j + 2]])
                if (board[i][j] == 1 and board[i + 1][j] == 2 and board[i + 2][j] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i, j, i + 2, j]])
        elif (i == (n - 1) and j == (n - 1)):
                if (board[i][j] == 1 and board[i][j - 1] == 2 and board[i][j - 2] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i, j, i, j - 2]])
                if (board[i][j] == 1 and board[i - 1][j] == 2 and board[i - 2][j] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i, j, i - 2, j]])
        elif (i == 0 and j == (n - 1)):
                if (board[i][j] == 1 and board[i][j - 1] == 2 and board[i][j - 2] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i, j, i, j - 2]])
                if (board[i][j] == 1 and board[i + 1][j] == 2 and board[i + 2][j] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i, j, i + 2, j]])                        
        elif (i == (n - 1) and j == 0):
                if (board[i][j] == 1 and board[i][j + 1] == 2 and board[i][j + 2] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i, j, i, j + 2]])
                if (board[i][j] == 1 and board[i - 1][j] == 2 and board[i - 2][j] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i, j, i - 2, j]])
        elif (j == 0):
                if (board[i][j] == 1 and board[i][j + 1] == 2 and board[i][j + 2] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i, j, i, j + 2]])
                if (board[i][j] == 1 and board[i - 1][j] == 2 and board[i - 2][j] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i, j, i - 2, j]])
                if (board[i][j] == 1 and board[i + 1][j] == 2 and board[i + 2][j] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i, j, i + 2, j]])
        elif (j == (n - 1)):
                if (board[i][j] == 1 and board[i][j - 1] == 2 and board[i][j - 2] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i, j, i, j - 2]])
                if (board[i][j] == 1 and board[i - 1][j] == 2 and board[i - 2][j] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i, j, i - 2, j]])
                if (board[i][j] == 1 and board[i + 1][j] == 2 and board[i + 2][j] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i, j, i + 2, j]])
        elif (i == 0 and (j >= 3 or n - j >= 3)):
                if (board[i][j] == 1 and board[i][j - 1] == 2 and board[i][j - 2] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i, j, i, j - 2]])
                if (board[i][j] == 1 and board[i][j + 1] == 2 and board[i][j + 2] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i, j, i, j + 2]])
                if (board[i][j] == 1 and board[i + 1][j] == 2 and board[i + 2][j] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i, j, i + 2, j]])
        elif (i == (n - 1)):
                if (board[i][j] == 1 and board[i][j - 1] == 2 and board[i][j - 2] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i, j, i, j - 2]])
                if (board[i][j] == 1 and board[i][j + 1] == 2 and board[i][j + 2] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i, j, i, j + 2]])
                if (board[i][j] == 1 and board[i - 1][j] == 2 and board[i - 2][j] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i, j, i - 2, j]])
        else:
                if (j >= 3 and board[i][j] == 1 and board[i][j - 1] == 2 and board[i][j - 2] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i, j, i, j - 2]])
                if ((n - j) >= 3 and board[i][j] == 1 and board[i][j + 1] == 2 and board[i][j + 2] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i, j, i, j + 2]])
                if ((i >= 3) and board[i][j] == 1 and board[i - 1][j] == 2 and board[i - 2][j] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i, j, i - 2, j]])
                if ((n - i) >= 3 and board[i][j] == 1 and board[i + 1][j] == 2 and board[i + 2][j] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i, j, i + 2, j]])
        lines.pop(0)
        return (lines)

def updateScoreO(board, n, i, j, scores, player):
        lines = [[]]
        if ((n - 1) > j > 0 and (n - 1) > i > 0):
                if (board[i][j] == 2 and board[i][j + 1] == 1 and board[i][j - 1] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i, j - 1, i, j + 1]])
                if (board[i][j] == 2 and board[i - 1][j] == 1 and board[i + 1][j] == 1):
                        scores[player - 1] = scores[player - 1] + 1
                        lines.extend([[i - 1, j, i + 1, j]])                                                
        '''elif ((n - 1) > j > 0)
        elif ((n - 1) > i > 0)'''
        lines.pop(0)
        return (lines)