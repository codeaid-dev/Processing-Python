x,y = 300,300

def setup():
    size(600,600)
    noStroke()

def draw():
    global x,y
    background(0)
    if keyPressed:
        if keyCode == UP:
            y -= 5
        if keyCode == DOWN:
            y += 5
        if keyCode == LEFT:
            x -= 5
        if keyCode == RIGHT:
            x += 5
    fill(255,255,0)
    arc(x,y,30,30,radians(45),radians(315))
