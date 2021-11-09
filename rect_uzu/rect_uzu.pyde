x,y = 0,0
row,col = 0,0
turn = 1
masu = [[0 for i in range(9)] for i in range(9)]
def setup():
    size(450,450)

def draw():
    global x,y,row,col,turn,masu
    if frameCount % 60 == 0:
        x = col%9*50
        y = row%9*50
        fill(255)
        rect(x,y,50,50)

        print(masu)

        if turn == 1 and (col == 8 or masu[col+1][row] == 1):
            masu[col][row] = 1
            row += 1
            turn = 2
        elif turn == 1:
            masu[col][row] = 1
            col += 1
        elif turn == 2 and (row == 8 or masu[col][row+1] == 1):
            masu[col][row] = 1
            col -= 1
            turn = 3
        elif turn == 2:
            masu[col][row] = 1
            row += 1
        elif turn == 3 and (col == 0 or masu[col-1][row] == 1):
            masu[col][row] = 1
            row -= 1
            turn = 4
        elif turn == 3:
            masu[col][row] = 1
            col -= 1
        elif turn == 4 and masu[col][row-1] == 1:
            masu[col][row] = 1
            col += 1
            turn = 1
        elif turn == 4:
            masu[col][row] = 1
            row -= 1
