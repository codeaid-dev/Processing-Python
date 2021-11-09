stars = []
class Star():
    pass

def setup():
    size(600,400)
    for i in range(100):
        s = Star()
        s.x = random(width)
        s.y = random(height)
        stars.append(s)

def draw():
    background(0)
    for s in stars:
        s.x += 1
        if s.x > width:
            s.x = 0
        noStroke()
        ellipse(s.x,s.y,5,5)
