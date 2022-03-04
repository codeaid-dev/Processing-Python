def setup():
    size(500,500)

def draw():
    background(255)
    fill(255,0,0)
    p=5
    for y in range(3):
        for x in range(3):
            polygon(100+x*150,100+y*150,50,p)
            p+=1

def polygon(x, y, radius, points):
    beginShape()
    for i in range(points):
        px = x + radius * cos(i * TWO_PI/points)
        py = y + radius * sin(i * TWO_PI/points)
        vertex(px,py)
    endShape(CLOSE)
