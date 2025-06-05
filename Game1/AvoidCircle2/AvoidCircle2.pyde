x,y,s = 250,400,50
up, down, left, right = False,False,False,False
def setup():
    size(500,800)
    noStroke()
def draw():
    global x,y
    background(255)

    fill(0,0,255)
    ellipse(x,y,s,s)

    if keyPressed:
        if up:
            y -= 3
        if down:
            y += 3
        if left:
            x -= 3
        if right:
            x += 3
    
    if x < s/2:
        x += 3
    if x > width-s/2:
        x -= 3
    if y < s/2:
        y += 3
    if y > height-s/2:
        y -= 3

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
