colors=[color(255,0,0),color(0,255,0),
        color(0,0,255),color(255,255,0),
        color(255,0,255),color(0,255,255),
        color(0),color(128,0,0),color(128)]
def setup():
    size(600,600)
    noStroke()

def draw():
    background(255)
    for i in range(16):
        fill(colors[8])
        ellipse(i%4*150+75,i/4*150+75,150,150)
