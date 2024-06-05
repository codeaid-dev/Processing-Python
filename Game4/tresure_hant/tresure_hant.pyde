xpos, ypos = 1,1
over = False
mazew,mazeh = 17,17
maze = [[0 for x in range(mazew)] for y in range(mazeh)]
def make_maze():
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    #周りの壁を作る
    for x in range(17):
        maze[0][x] = 1
        maze[mazeh-1][x] = 1
    for y in range(1,mazeh-1):
        maze[y][0] = 1
        maze[y][mazew-1] = 1
    #内側をクリアする
    for y in range(1,mazeh-1):
        for x in range(1,mazew-1):
            maze[y][x] = 0
    #柱を建てて壁を作る
    for y in range(2,mazeh-2,2):
        for x in range(2,mazew-2,2):
            maze[y][x] = 1
            d = int(random(3))
            if y == 2:
                d = int(random(4))
            maze[y+dy[d]][x+dx[d]] = 1

#宝をセットする
tresurex,tresurey = 1,1
def set_tresure():
    global tresurex,tresurey
    while True:
        tresurex = int(random(1,mazew-1))
        tresurey = int(random(1,mazeh-1))
        if maze[tresurey][tresurex] == 0:
            maze[tresurey][tresurex] = 2
            break

def setup():
    size(680,680)
    make_maze()
    set_tresure()
    noStroke()

def draw():
    global over
    background(255)
    fill(200)
    for y in range(17):
        for x in range(17):
            if maze[y][x] == 1:
                rect(x*40, y*40, 40, 40)
    if over:
        fill(255, 0, 0)
    else:
        fill(0,255,0)
    ellipse(xpos*40+20, ypos*40+20, 40, 40)

    if maze[ypos][xpos] == 2:
        textSize(30)
        textAlign(CENTER)
        text("FIND!!",width/2,height/2)
        over = True
        return

def keyPressed():
    global xpos,ypos
    if over:
        return
    dx, dy = xpos, ypos
    if keyCode == UP:
        dy -= 1
    if keyCode == DOWN:
        dy += 1
    if keyCode == LEFT:
        dx -= 1
    if keyCode == RIGHT:
        dx += 1
    if 0 <= dx < 16 and 0 <= dy < 16:
        if maze[dy][dx] != 1:
            xpos = dx
            ypos = dy
