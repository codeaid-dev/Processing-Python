def setup():
    size(500,500)

def draw():
    background(255)
    fill(255,0,0)
    polygon(width/2,height/2,100,5)

def polygon(x, y, radius, points):
    beginShape()
    for i in range(points):
        px = x + radius * cos(i * TWO_PI/points)
        py = y + radius * sin(i * TWO_PI/points)
        vertex(px,py)
    endShape(CLOSE)
