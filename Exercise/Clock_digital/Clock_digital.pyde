def setup():
    size(600,200)
    frameRate(1)

def draw():
    background(0)
    h = hour()
    m = minute()
    s = second()
    fill(255)
    textAlign(CENTER)
    textSize(150)
    text("{}:{}:{}".format(h,m,s),width/2,150)
