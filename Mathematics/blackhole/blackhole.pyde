class Circle:
    pass

ens = []
def setup():
    size(600,600)
    for i in range(30):
        en = Circle()
        en.angle = random(360)
        en.distance = width/2
        en.diameter = width/4
        en.speed = random(1,4)
        ens.append(en)

def draw():
    background(0)
    for en in ens:
        if en.distance > 0:
            en.distance -= en.speed
            en.diameter -= en.speed/2
            x = width/2 + en.distance*cos(en.angle*PI/180)
            y = height/2 + en.distance*sin(en.angle*PI/180)
            fill(0,255,0)
            ellipse(x,y,en.diameter,en.diameter)
        else:
            en.angle = random(360)
            en.distance = width/2
            en.diameter = width/4
            en.speed = random(1,4)
