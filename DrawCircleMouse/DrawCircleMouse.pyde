x, y = 0, 0

def setup():
    size(300, 300)
    background(0)

def draw():
    fill(255, 255, 0)

def mousePressed():
    global x, y
    x = mouseX
    y = mouseY

def mouseDragged():
    dst = dist(x, y, mouseX, mouseY)
    ellipse(x, y, dst*2, dst*2)
