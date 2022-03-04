px=[0 for i in range(5)]
py=[0 for i in range(5)]
def setup():
    size(500,500)

def draw():
    background(255)
    polygon(width/2,height/2,100,5)

def polygon(x, y, radius, points):
    for i in range(points):
        px[i] = x + radius * cos(i * TWO_PI/points)
        py[i] = y + radius * sin(i * TWO_PI/points)
    n = len(px)
    for i in range(n):
        line(px[i%n],py[i%n],px[(i+1)%n],py[(i+1)%n])
