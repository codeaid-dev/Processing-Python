def setup():
    size(720,200)
    colorMode(HSB,360,100,100)
def draw():
    for i in range(360):
        strokeWeight(2)
        stroke(i,100,100)
        line(i*2,0,i*2,height)
