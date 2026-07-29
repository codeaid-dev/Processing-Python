def setup():
    size(500,500)

def draw():
    background(0)
    stroke(255)
    f = color(255,0,0)
    t = color(255,255,0)
    for i in range(5):
        amt = map(i,0,5,0.0,1.0)
        inter = lerpColor(f,t,amt)
        fill(inter)
        rect(i*100,0,100,height)
