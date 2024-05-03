x = 300
y = 200
def setup():
    size(600,400)

def draw():
    global rad
    background(0)
    fill(255)
    rectMode(CENTER)
    translate(x,y)
    rad = radians(45)
    rotate(rad)
    rect(0,0,50,50)
