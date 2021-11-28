x,y = 250,250
speed = 3
def setup():
    size(500,500)

def draw():
    global x,y
    background(255)
    if keyPressed:
        if keyCode == LEFT:
            x -= speed
        elif keyCode == RIGHT:
            x += speed
        elif keyCode == UP:
            y -= speed
        elif keyCode == DOWN:
            y += speed
    fill(0)
    ellipse(x,y,50,50)
