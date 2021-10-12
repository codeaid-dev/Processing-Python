maze = [[0 for x in range(15)] for y in range(15)]
xpos, ypos = 0, 0
atari_x = 0
atari_y = 0
over = False
timer = 600

def setup():
    global atari_x, atari_y
    noStroke()
    size(600, 600)
    for y in range(15):
        for x in range(15):
            if x % 2 == 1 and y % 2 == 1:
                maze[y][x] = 1
                d = int(random(3))
                if y == 1:
                    d = int(random(4))

                dx, dy = 0, 0                    
                if d == 0:
                    dx = -1
                elif d == 1:
                    dx = 1
                elif d == 2:
                    dy = 1
                elif d == 3:
                    dy = -1
                maze[y+dy][x+dx] = 1

    while True:
        atari_x = int(random(3,15))
        atari_y = int(random(3,15))
        if maze[atari_y][atari_y] == 0:
            maze[atari_y][atari_x] = 2
            break

def keyPressed():
    if over:
        return

    global xpos,ypos
    dx, dy = xpos, ypos
    if keyCode == UP:
        dy -= 1
    if keyCode == DOWN:
        dy += 1
    if keyCode == LEFT:
        dx -= 1
    if keyCode == RIGHT:
        dx += 1
    if 0 <= dx < 15 and 0 <= dy < 15:
        if maze[dy][dx] != 1:
            xpos = dx
            ypos = dy

def draw():
    global over, timer
    background(128)
    fill(255)
    for y in range(15):
        for x in range(15):
            if maze[y][x] == 1:
                rect(x*40, y*40, 40, 40)

    if over:
        fill(255, 0, 0)
    else:
        fill(0, 255, 0)
    ellipse(xpos*40 + 20, ypos*40+20, 30, 30)

    if maze[ypos][xpos] == 2:
        textSize(30)
        textAlign(CENTER)
        text("FIND!!",width/2,height/2)
        over = True
        return

    fill(255,0,0,128)
    rect(0,0,timer,20)
    timer -= 0.1
    if timer < 0:
        textSize(30)
        textAlign(CENTER)
        text("GAME OVER",width/2,height/2)
        over = True
        return
