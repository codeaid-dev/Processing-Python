x1,y1,x2,y2,x3,y3 = 250,100,100,400,400,250
dx1,dy1,dx2,dy2,dx3,dy3 = 2,3,2,3,2,3

def setup():
    size(500,500)
    strokeWeight(5)
    stroke(255)

def draw():
    global x1,y1,x2,y2,x3,y3,dx1,dy1,dx2,dy2,dx3,dy3
    background(0)
    x1 += dx1
    y1 += dy1
    x2 += dx2
    y2 += dy2
    x3 += dx3
    y3 += dy3
    if x1 > width or x1 < 0:
        dx1 *= -1
    if x2 > width or x2 < 0:
        dx2 *= -1
    if x3 > width or x3 < 0:
        dx3 *= -1
    if y1 > height or y1 < 0:
        dy1 *= -1
    if y2 > height or y2 < 0:
        dy2 *= -1
    if y3 > height or y3 < 0:
        dy3 *= -1

    fill(255,0,0)
    triangle(x1, y1, x2, y2, x3, y3)
