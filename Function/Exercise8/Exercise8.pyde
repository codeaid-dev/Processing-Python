def setup():
    size(500,500)
def draw():
    fill(255)
def mousePressed():
    draw_ufo(mouseX,mouseY)
def draw_ufo(x,y):
    strokeWeight(5)
    fill(255)
    ellipse(x-50,y+10,50,50)
    ellipse(x,y+20,50,50)
    ellipse(x+50,y+10,50,50)
    ellipse(x,y,200,50)
    ellipse(x,y-25,120,50)
