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
