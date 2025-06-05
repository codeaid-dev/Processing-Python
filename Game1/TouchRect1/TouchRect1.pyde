px, py, ps = 0, 0, 0
sx, sy = 0, 0
up, down, left, right = False,False,False,False

def setup():
    global px, py, ps
    size(600, 500)
    px = width/2
    py = height/2
    ps = 30

def draw():
    global px, py, ps, sx, sy
    background(255)
    fill(0)
    ellipse(px, py, ps, ps)

    if keyPressed:
        if up:
            sy -= 1
        if down:
            sy += 1
        if left:
            sx -= 1
        if right:
            sx += 1

    sx *= 0.98
    sy *= 0.98
    px += sx
    py += sy

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
