def setup():
    size(600,300)

def draw():
    background(0);
    for i in range(width+1):
        c = map(i,0,width,0,255)
        stroke(c)
        line(i,0,i,height)
