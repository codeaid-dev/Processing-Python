x,y,s = 250,400,50
def setup():
    size(500,800)
    noStroke()
def draw():
    global x,y
    background(255)

    fill(0,0,255)
    ellipse(x,y,s,s)

    if keyPressed:
        if keyCode == RIGHT:
            x += 3
        if keyCode == LEFT:
            x -= 3
        if keyCode == UP:
            y -= 3
        if keyCode == DOWN:
            y += 3
        
