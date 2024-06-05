x,y,s = 300,200,30
dx,dy = 0,0

def setup():
    size(600,400)

def draw():
    global x,y,dx,dy
    background(255)
    noStroke()
    fill(0,0,255)
    ellipse(x,y,s,s)

    if y > height-s/2:
        dy = 0
        y = height-s/2
    else:
        dy += 0.3

    if keyPressed:
        if keyCode == UP and dy == 0:
            dy = -12
        if keyCode == DOWN:
            dy += 2
        if keyCode == LEFT:
            dx -= 0.1
        if keyCode == RIGHT:
            dx += 0.1

    dx *= 0.98
    x += dx
    y += dy
