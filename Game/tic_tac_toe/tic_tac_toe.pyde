tiles = []
piece = [None for i in range(9)]
turn = True #True:O, False:X
wins = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
        ]
winner = None

def setup():
    size(450,450)
    textSize(75)
    textAlign(CENTER)
    strokeWeight(3)
    line(width/3,0,width/3,height)
    line(width/3*2,0,width/3*2,height)
    line(0,height/3,width,height/3)
    line(0,height/3*2,width,height/3*2)
    for i in range(9):
        tiles.append(PVector(75+i%3*150,75+i/3*150))

def draw():
    for i in range(9):
        if piece[i] != None:
            if winner and i in winner:
                fill(255,0,0)
            else:
                fill(0)
            text(piece[i],tiles[i].x,tiles[i].y+30)

def mousePressed():
    global turn
    x = mouseX
    y = mouseY
    for i in range(9):
        if tiles[i].x-75<x<tiles[i].x+75 \
        and tiles[i].y-75<y<tiles[i].y+75:
            if piece[i] == None:
                if turn:
                    piece[i] = 'O'
                    turn = False
                else:
                    piece[i] = 'X'
                    turn = True
    if winner == None:
        check()

def check():
    global winner
    for i in range(len(wins)):
        a = wins[i][0]
        b = wins[i][1]
        c = wins[i][2]
        if piece[a] \
            and piece[a]==piece[b] \
            and piece[a]==piece[c]:
            winner = wins[i]
