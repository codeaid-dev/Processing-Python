x,y = 250,250
up,down,left,right = False,False,False,False

def setup():
    size(500,500)
def draw():
    global x,y
    background(255)
    if up:
        y -= 5
    if down:
        y += 5
    if left:
        x -= 5
    if right:
        x += 5
    fill(0,0,255)
    ellipse(x,y,30,30)

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
