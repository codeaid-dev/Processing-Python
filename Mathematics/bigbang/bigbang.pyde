class Circle:
    pass

ens = []
def setup():
    size(500,500)
    for i in range(500):
        en = Circle()
        en.angle = random(360)
        en.distance = 0
        en.diameter = random(5,20)
        en.speed = random(1,5)
        ens.append(en)
    noStroke()
    fill(255,128)

def draw():
    background(0)
    for en in ens:
        x = width/2 + en.distance*cos(en.angle*PI/180)
        y = height/2 + en.distance*sin(en.angle*PI/180)
        ellipse(x,y,en.diameter,en.diameter)
        if x < 0 or x > width or y < 0 or y > height:
            en.angle = random(360)
            en.distance = 0
            en.diameter = random(5,20)
            en.speed = random(1,5)
        else:
            en.distance += en.speed
