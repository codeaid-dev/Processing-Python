radius = 255
rgb = [color(255,0,0),
       color(255,165,0),
       color(255,255,0),
       color(0,128,0),
       color(0,255,255),
       color(0,0,255),
       color(128,0,128)]

def setup():
    size(500,300)
    background(255)
#    colorMode(HSB,7,255,255)

def draw():
    global radius
    if radius > 185:
        index = (255-radius)//10
#        c = color(index,255,255)
        for i in range(180,360):
            x = width/2 + radius*cos(radians(i))
            y = height + radius*sin(radians(i))
            strokeWeight(5)
            stroke(rgb[index])
#            stroke(c)
            point(x,y)
        radius -= 1
