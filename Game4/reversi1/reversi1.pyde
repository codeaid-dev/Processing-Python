GRID_SIZE = 8
CELL_SIZE = 100
EMPTY = 0
BLACK = 1
WHITE = 2
board = [[EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
board[3][3] = WHITE
board[4][4] = WHITE
board[3][4] = BLACK
board[4][3] = BLACK

def setup():
    size(GRID_SIZE*CELL_SIZE, GRID_SIZE*CELL_SIZE)
    noLoop()

def draw():
    draw_board()
    draw_pieces()

def draw_board():
    background(0,128,0)
    stroke(0)
    strokeWeight(2)
    for i in range(GRID_SIZE+1):
        line(i*CELL_SIZE, 0, i*CELL_SIZE, height)
        line(0, i*CELL_SIZE, width, i*CELL_SIZE)

def draw_pieces():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] == BLACK:
                fill(0)
                ellipse(i*CELL_SIZE+CELL_SIZE/2,
                        j*CELL_SIZE+CELL_SIZE/2,
                        CELL_SIZE-10, CELL_SIZE-10)
            elif board[i][j] == WHITE:
                fill(255)
                ellipse(i*CELL_SIZE+CELL_SIZE/2,
                        j*CELL_SIZE+CELL_SIZE/2,
                        CELL_SIZE-10, CELL_SIZE-10)
