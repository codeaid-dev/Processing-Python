x1,y1,x2,y2 = 100,100,400,400
dx1,dy1,dx2,dy2 = 2,3,2,3

def setup():
    size(500,500)
    strokeWeight(5)
    stroke(255)

def draw():
    global x1,y1,x2,y2,dx1,dy1,dx2,dy2
    background(0)
    x1 += dx1
    y1 += dy1
    x2 += dx2
    y2 += dy2
    if x1 > width or x1 < 0:
        dx1 *= -1
    if x2 > width or x2 < 0:
        dx2 *= -1
    if y1 > width or y1 < 0:
        dy1 *= -1
    if y2 > width or y2 < 0:
        dy2 *= -1

    line(x1, y1, x2, y2)
