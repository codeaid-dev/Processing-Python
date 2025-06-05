x,y = 300,300
up,down,left,right = False,False,False,False

def setup():
    size(600,600)
    noStroke()

def draw():
    global x,y
    background(0)
    if keyPressed:
        if up:
            y -= 5
        if down:
            y += 5
        if left:
            x -= 5
        if right:
            x += 5
    fill(255,255,0)
    arc(x,y,30,30,radians(45),radians(315))

def keyPressed():
    global up,down,left,right
    if keyCode == UP:
        up = True
    if keyCode == DOWN:
        down = True
    if keyCode == LEFT:
        left = True
    if keyCode == RIGHT:
        right = True

def keyReleased():
    global up,down,left,right
    if keyCode == UP:
        up = False
    if keyCode == DOWN:
        down = False
    if keyCode == LEFT:
        left = False
    if keyCode == RIGHT:
        right = False
