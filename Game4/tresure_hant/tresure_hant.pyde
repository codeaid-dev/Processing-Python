xpos, ypos = 0,0
over = False
mazew,mazeh = 15,15
maze = [[0 for x in range(mazew)] for y in range(mazeh)]
start=0
passed=0

def make_maze():
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    for y in range(1,mazeh-1,2):
        for x in range(1,mazew-1,2):
            maze[y][x] = 1
            d = int(random(3))
            if y == 1:
                d = int(random(4))
            maze[y+dy[d]][x+dx[d]] = 1

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
    global start
    size(600,600)
    noStroke()
    make_maze()
    set_tresure()
    start = millis()

def draw():
    global over,passed
    background(255)
    fill(128)
    for y in range(mazew):
        for x in range(mazeh):
            if maze[y][x] == 1:
                rect(x*40, y*40, 40, 40)
    if over:
        fill(255, 0, 0)
    else:
        fill(0,255,0)
    ellipse(xpos*40+20, ypos*40+20, 30, 30)

    if maze[ypos][xpos] == 2:
        textSize(30)
        textAlign(CENTER)
        text("FIND!!",width/2,height/2)
        if passed == 0:
            passed = (millis()-start)/1000.0
        text(passed,width/2,height/2+40)
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
    if 0 <= dx < mazew and 0 <= dy < mazeh:
        if maze[dy][dx] != 1:
            xpos = dx
            ypos = dy
