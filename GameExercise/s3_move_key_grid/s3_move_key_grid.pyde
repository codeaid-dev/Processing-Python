x,y=0,0
def setup():
    size(600,600)

def draw():
    background(255)
    noStroke()
    fill(0)
    rect(x,y,50,50)

def keyPressed():
    global x,y
    if keyCode == UP:
        y -= 50
        if y < 0:
            y += 50
    if keyCode == DOWN:
        y += 50
        if y > height-50:
            y -= 50
    if keyCode == LEFT:
        x -= 50
        if x < 0:
            x += 50
    if keyCode == RIGHT:
        x += 50
        if x > width-50:
            x -= 50
