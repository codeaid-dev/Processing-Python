def setup():
    size(500, 500)

def draw():
    background(255)
    x, y = mouseX, mouseY
    mato(x-70, y, 100)
    mato(x+70, y, 100)

def mato(x, y, w):
    fill(255)
    strokeWeight(w/10)
    ellipse(x, y, w, w)
    strokeWeight(w/20)
    ellipse(x, y, w/6*4, w/6*4)
    strokeWeight(w/10)
    ellipse(x, y, w/3.5, w/3.5)
