def setup():
    size(300, 200)

def draw():
    background(255)
    if mouseX > width/3*2:
        fill(0, 255, 0)
        ellipse(width/6*5, height/2, 100, 100)
    elif mouseX > width/3:
        fill(255, 255, 0)
        ellipse(width/6*3, height/2, 100, 100)
    else:
        fill(255, 0, 0)
        ellipse(width/6, height/2, 100, 100)
