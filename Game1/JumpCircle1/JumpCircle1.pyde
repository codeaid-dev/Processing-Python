x,y,s = 300,200,30
up, down, left, right = False,False,False,False
dx,dy = 0,0

def setup():
    size(600,400)

def draw():
    global x,y,dx,dy
    background(255)
    noStroke()
    fill(0,0,255)
    ellipse(x,y,s,s)

    if y > height-s/2:
        dy = 0
        y = height-s/2
    else:
        dy += 0.3

    if keyPressed:
        if up and dy == 0:
            dy = -12
        if down:
            dy += 2
        if left:
            dx -= 0.1
        if right:
            dx += 0.1

    dx *= 0.98
    x += dx
    y += dy

def keyPressed():
    global up, down, left, right
    if keyCode == UP:
        up = True
    if keyCode == DOWN:
        down = True
    if keyCode == LEFT:
        left = True
    if keyCode == RIGHT:
        right = True

def keyReleased():
    global up, down, left, right
    if keyCode == UP:
        up = False
    if keyCode == DOWN:
        down = False
    if keyCode == LEFT:
        left = False
    if keyCode == RIGHT:
        right = False
