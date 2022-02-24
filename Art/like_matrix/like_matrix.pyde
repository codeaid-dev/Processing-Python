circles = []
def setup():
    size(800, 600)
    noStroke()
    frameRate(30)

def draw():
    fill(0,0,0,10)
    rect(0,0,width,height)
    obj = PVector(random(0, width), 0)
    obj.dy = 5
    circles.append(obj)
    for c in circles:
        fill(0,255,0)
        ellipse(c.x, c.y, 10, 10)
        c.y += c.dy
        if c.y > height:
            circles.remove(c)
