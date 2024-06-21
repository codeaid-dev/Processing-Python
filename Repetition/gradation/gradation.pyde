def setup():
    size(500,500)

def draw():
    strokeWeight(2)
    for i in range(250):
        stroke(i)
        line(0,i*2,width,i*2)
