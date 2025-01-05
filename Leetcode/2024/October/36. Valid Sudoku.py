board = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
       [".", "4", ".", "3", ".", ".", ".", ".", "."],
       [".", ".", ".", ".", ".", "3", ".", ".", "1"],
       ["8", ".", ".", ".", ".", ".", ".", "2", "."],
       [".", ".", "2", ".", "7", ".", ".", ".", "."],
       [".", "1", "5", ".", ".", ".", ".", ".", "."],
       [".", ".", ".", ".", ".", "2", ".", ".", "."],
       [".", "2", ".", "9", ".", ".", ".", ".", "."],
       [".", ".", "4", ".", ".", ".", ".", ".", "."]]

def col_check(board):
    for i in range(9):
        col = []
        for j in range(9):
            if board[j][i] != '.':
                col.append(board[j][i])
        if len(col) != len(set(col)):
            return False
    return True

def row_check(board):
    for i in range(9):
        row = []
        for j in range(9):
            if board[i][j] != '.':
                row.append(board[i][j])
        if len(row) != len(set(row)):
            return False
    return True

def box_check(board):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = []
            for k in range(3):
                for l in range(3):
                    if board[i+k][j+l] != '.':
                        box.append(board[i+k][j+l])
            if len(box) != len(set(box)):
                return False
    return True
print(col_check(board) and row_check(board) and box_check(board))
