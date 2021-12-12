def setup():
    size(500,500)

def draw():
    background(200)
    x = width/8
    y = height/8
    s = width/4
    for i in range(4):
        ellipse(x+s*i,y+s*i,s,s)
