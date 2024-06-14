GRID_SIZE = 8
CELL_SIZE = 100
EMPTY = 0
BLACK = 1
WHITE = 2
board = [[EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
current_player = BLACK
DIR8 = [(-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)]

def setup():
    size(GRID_SIZE*CELL_SIZE, GRID_SIZE*CELL_SIZE)
    reset()
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

def mousePressed():
    global current_player
    x = mouseX//CELL_SIZE
    y = mouseY//CELL_SIZE

    if valid_move(x, y, current_player):
        make_move(x, y, current_player)
        current_player = \
        WHITE if current_player==BLACK else BLACK
        redraw()

def valid_move(x, y, player):
    if board[x][y] != EMPTY:
        return False

    for dx,dy in DIR8:
        nx,ny = x+dx,y+dy
        if on_board(nx, ny) and \
            board[nx][ny] == (WHITE if player==BLACK else BLACK):
            while on_board(nx, ny) and board[nx][ny] != EMPTY:
                if board[nx][ny] == player:
                    return True
                nx+=dx
                ny+=dy
    return False

def on_board(x, y):
    return 0<=x<GRID_SIZE and 0<=y<GRID_SIZE

def make_move(x, y, player):
    board[x][y] = player
    for dx, dy in DIR8:
        flip_pieces(x, y, dx, dy, player)

def flip_pieces(x, y, dx, dy, player):
    nx,ny = x+dx,y+dy
    pieces_to_flip = []
    
    while on_board(nx, ny) and \
            board[nx][ny] == (WHITE if player==BLACK else BLACK):
        pieces_to_flip.append((nx, ny))
        nx+=dx
        ny+=dy
    
    if on_board(nx, ny) and board[nx][ny] == player:
        for fx, fy in pieces_to_flip:
            board[fx][fy] = player

def keyPressed():
    if key == 'r':
        reset()
        redraw()

def reset():
    global current_player
    current_player = BLACK
    for i in range(GRID_SIZE*GRID_SIZE):
        x,y = i%8,i//8
        board[x][y] = 0
    board[3][3] = WHITE
    board[4][4] = WHITE
    board[3][4] = BLACK
    board[4][3] = BLACK
