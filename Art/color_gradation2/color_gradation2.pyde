def setup():
    size(500,500)
    noStroke()

def draw():
    background(255);
    for i in range(width,0,-1):
        c = map(i,0,width,0,255)
        fill(c)
        ellipse(width/2,height/2,i,i)
