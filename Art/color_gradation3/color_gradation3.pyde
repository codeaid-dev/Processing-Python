def setup():
    size(300,300)

def draw():
    background(255)
    f = color(255,0,0)
    t = color(255,255,0)
    for i in range(width):
        amt = map(i,0,width,0.0,1.0)
        inter = lerpColor(f,t,amt)
        stroke(inter)
        line(i,0,i,height)
