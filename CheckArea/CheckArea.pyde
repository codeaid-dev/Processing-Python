def setup():
    size(300, 300)

def draw():
    background(255)
    line(width/2, 0, width/2, height)
    line(0, height/2, width, height/2)
    if mouseX > width/2 or mouseY > height/2:
        fill(0, 255, 0)
        rect(width/2, 0, width/2, height/2)
        rect(0, height/2, width/2, height/2)
        rect(width/2, height/2, width/2, height/2)
