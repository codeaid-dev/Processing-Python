move = 1
x = 100
def setup():
    size(500, 200)

def draw():
    global move, x
    x += move
    background(255)
    mato(x, height/2, 100)

def mato(x, y, w):
    fill(255)
    strokeWeight(w/10)
    ellipse(x, y, w, w)
    strokeWeight(w/20)
    ellipse(x, y, w/6*4, w/6*4)
    fill(0)
    ellipse(x, y, w/3, w/3)
    fill(255)
    ellipse(x, y, w/4, w/4)
