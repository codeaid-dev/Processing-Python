x,y = 0,0
speed = 5
state = 0
w,h = 100,100

def setup():
    size(500,500)

def draw():
    global x,y,state
    background(255)
    noStroke()
    fill(0)
    rect(x,y,w,h)
    if state == 0:
        x += speed
        if x>width-w:
            x = width-w
            state = 1
    elif state == 1:
        y += speed
        if y>height-h:
            y = height-h
            state = 2
    elif state == 2:
        x -= speed
        if x<0:
            x = 0
            state = 3
    elif state == 3:
        y -= speed
        if y<0:
            y = 0
            state = 0
