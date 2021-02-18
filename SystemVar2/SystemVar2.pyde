def setup():
    size(500, 500)
    
def draw():
    background(255)
    line(mouseX, 0, mouseX, height)
    line(0, mouseY, width, mouseY)
    fill(0, 0, 0, 20)
    ellipse(mouseX, mouseY, 50, 50)
