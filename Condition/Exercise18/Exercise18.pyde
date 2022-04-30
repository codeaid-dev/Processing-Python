x,y = 250,0
speed = 0
gravity = 0.1

def setup():
    size(500,500)

def draw():
    global y,speed
    background(255)
    fill(0)
    noStroke()
    ellipse(x,y,50,50)
    y += speed
    speed += gravity
    if y>height-25:
        y = height-25

def keyPressed():
    global speed
    if keyCode == UP and y == height-25:
        speed = -8
