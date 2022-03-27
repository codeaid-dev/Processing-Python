x, y = 0, 0
def setup():
    size(500, 500)
    background(0)
    fill(255, 255, 0)

def draw():
    pass

def mousePressed():
    global x, y
    x = mouseX
    y = mouseY

def mouseDragged():
    dst = dist(x, y, mouseX, mouseY)
    ellipse(x, y, dst*2, dst*2)

def keyPressed():
    if key == 'c':
        background(0)
    if key == 'r':
        fill(255, 0, 0)
    elif key == 'g':
        fill(0, 255, 0)
    elif key == 'b':
        fill(0, 0, 255)
    else:
        fill(255, 255, 0)
