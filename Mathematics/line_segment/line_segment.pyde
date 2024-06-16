def setup():
    size(500,500)

def draw():
    background(200)
    x0 = 120.0
    y0 = 120.0
    x1 = mouseX
    y1 = mouseY

    x2 = 120.0
    y2 = 360.0
    x3 = 360.0
    y3 = 120.0

    if abs(x1-x0) < 0.01:
        x1 = x0+0.01
    if abs(x3-x2) < 0.01:
        x3 = x2+0.01

    t0 = (y1-y0)/(x1-x0)
    t1 = (y3-y2)/(x3-x2)

    x = 0
    y = 0
    if t0 != t1:
        x = (y2-y0+t0*x0-t1*x2)/(t0-t1)
        y = t0*(x-x0)+y0

    r0 = (x-x0)/(x1-x0)
    r1 = (x-x2)/(x3-x2)
    hit = 0<r0<1 and 0<r1<1
    strokeWeight(3)
    line(x0,y0,x1,y1)
    line(x2,y2,x3,y3)

    if hit and t0 != t1:
        strokeWeight(24)
        point(x,y)
