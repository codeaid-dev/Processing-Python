x,y = 50,50
speed = 3
def setup():
    size(500,500)

def draw():
    global x,y
    background(255)
    fill(255,0,0)
    rect(150,150,200,200)
    if keyPressed:
        if keyCode == LEFT:
            x -= speed
            if x-25 < 0:
                x += speed
        elif keyCode == RIGHT:
            x += speed
            if x+25 > width:
                x -= speed
        elif keyCode == UP:
            y -= speed
            if y-25 < 0:
                y += speed
        elif keyCode == DOWN:
            y += speed
            if y+25 > height:
                y -= speed
        if x+25>150 and x-25<350 and y+25>150 and y-25<350:
            if keyCode == LEFT:
                x += speed
            if keyCode == RIGHT:
                x -= speed
            if keyCode == UP:
                y += speed
            if keyCode == DOWN:
                y -= speed

    fill(0)
    ellipse(x,y,50,50)
