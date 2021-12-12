x = 150
def setup():
    size(300, 300)

def draw():
    global x
    background(0)
    fill(255,0,0)
    ellipse(x, height/2, 40, 40)

def mousePressed():
    global x
    x += 5

def keyPressed():
    global x
    x -= 5
