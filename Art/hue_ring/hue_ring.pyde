def setup():
    size(500,500)
    colorMode(HSB,360,100,100)

def draw():
    radius = 200
    angle = 0
    background(0,0,255)
    for i in range(360):
        x = width/2 + radius * cos(radians(angle))
        y = height/2 + radius * sin(radians(angle))
        strokeWeight(5)
        stroke(i,100,100)
        line(width/2,height/2,x,y)
        angle += 1
