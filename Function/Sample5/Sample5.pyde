def setup():
    size(500, 500)

def draw():
    background(255)
    line(mouseX, mouseY, width/4, height/2)
    line(mouseX, mouseY, width/2, height/4)
    line(mouseX, mouseY, width/4*3, height/2)
    line(mouseX, mouseY, width/2, height/4*3)
