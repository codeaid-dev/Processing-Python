x, y = 0, 0
k = 0

def setup():
    size(300, 300)
    background(0)

def draw():
    global k
    if k == 'r':
        fill(255, 0, 0)
    elif k == 'g':
        fill(0, 255, 0)
    elif k == 'b':
        fill(0, 0, 255)
    else:
        fill(255, 255, 0)

def mousePressed():
    global x, y
    x = mouseX
    y = mouseY

def mouseDragged():
    dst = dist(x, y, mouseX, mouseY)
    ellipse(x, y, dst*2, dst*2)

def keyPressed():
    global k
    if key == 'c':
        background(0)
    if key == 'r':
        k = 'r'
    elif key == 'g':
        k = 'g'
    elif key == 'b':
        k = 'b'
    else:
        k = 0
