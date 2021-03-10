def setup():
    size(500, 500)

def draw():
    background(0)
    if mouseX < width/2 and mouseY < height/2:
        fill(255, 0, 0)
    elif mouseX < width/2 and mouseY > height/2:
        fill(0, 255, 0)
    elif mouseX > width/2 and mouseY < height/2:
        fill(0, 0, 255)
    else:
        fill(255, 255, 0)
    ellipse(mouseX, mouseY, 50, 50)
