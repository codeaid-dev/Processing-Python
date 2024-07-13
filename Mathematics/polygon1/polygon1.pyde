def setup():
    size(500,500)

def draw():
    background(255)
    polygon(width/2,height/2,100,5)

def polygon(x, y, radius, points):
    for i in range(points):
        px = x + radius * cos(i * TWO_PI/points)
        py = y + radius * sin(i * TWO_PI/points)
        fill(0)
        ellipse(px,py,10,10)
