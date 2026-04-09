def setup():
    size(500,500)

def draw():
    s = second()
    m = minute()
    h = hour() % 12
    hangle = h*30-90
    mangle = m*6-90
    sangle = s*6-90
    background(255)
    strokeWeight(5)
    hx = width/2+150*cos(radians(hangle))
    hy = height/2+150*sin(radians(hangle))
    line(width/2,height/2,hx,hy)
    strokeWeight(3)
    mx = width/2+200*cos(radians(mangle))
    my = height/2+200*sin(radians(mangle))
    line(width/2,height/2,mx,my)
    strokeWeight(2)
    sx = width/2+200*cos(radians(sangle))
    sy = height/2+200*sin(radians(sangle))
    line(width/2,height/2,sx,sy)
