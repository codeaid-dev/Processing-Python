stars = []
class Star():
    pass

def setup():
    global stars
    size(600,400)
    for i in range(100):
        s = Star()
        s.x = random(width)
        s.y = random(height)
        s.speed = random(1,6)
        stars.append(s)

def draw():
    background(0)
    for s in stars:
        s.x -= s.speed
        if s.x < 0:
            s.x = width
        noStroke()
        fill(255,255,255,s.speed/5*255)
        ellipse(s.x,s.y,5,5)
