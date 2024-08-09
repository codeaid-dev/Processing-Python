class Circle:
    pass
ens = []
def setup():
    size(600,600)
    for i in range(10):
        en = Circle()
        en.x = width/2
        en.y = height/2
        en.angle = random(360)
        en.speed = random(2,6)
        en.size = 30
        en.color = color(0,255,0)
        ens.append(en)

def draw():
    background(255)
    for en in ens:
        en.x += en.speed * cos(en.angle*PI/180)
        en.y += en.speed * sin(en.angle*PI/180)
        if en.x < en.size/2 or en.x > width-en.size/2:
            en.angle = 180-en.angle
        if en.y < en.size/2 or en.y > height-en.size/2:
            en.angle *= -1
        noStroke()
        fill(en.color)
        ellipse(en.x,en.y,en.size,en.size)
