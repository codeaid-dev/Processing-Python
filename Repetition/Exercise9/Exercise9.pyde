def setup():
    size(600,300)

def draw():
    background(200)
    for i in range(5):
        x = i*100+50
        s = i*50+50
        fill(i*63)
        ellipse(x,150,s,s)
