board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"


def adj(row, col):
    def ch(q, y):
        if q > -1 and y > -1:
            x.append([q, y])

    x = []

    ch(row + 1, col)
    ch(row - 1, col)
    ch(row, col + 1)
    ch(row, col - 1)

    return x

def ch2(i,j,c=1):
    b = False
    for pos in adj(i,j):
        if board[pos[0]][pos[1]] == word[c]:
            b = True
            break
    if b:
        if c == len(word):
            return True
        else:
            ch2(pos[0],pos[1],c+1)
    else:
        return False


for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j] == word[0]:
            print(board[i][j])
            ch2(i,j)
