def setup():
    size(600, 600)
    noStroke()

def draw():
    fill(0,0,0,10)
    rect(0,0,width,height)
    x = random(0, width)
    y = random(0, height)
    fill(random(0,256),random(0,256),random(0,256))
    d = random(10,50)
    ellipse(x, y, d, d)
