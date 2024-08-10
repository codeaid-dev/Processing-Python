class Circle:
    pass
ens = []
def setup():
    size(600,600)
    for i in range(10):
        en = Circle()
        en.x = width/2
        en.y = height/2
        en.angle = random(TWO_PI)
        en.speed = random(2,6)
        en.radius = 15
        en.color = color(0,255,0)
        ens.append(en)

def draw():
    background(255)
    for en in ens:
        en.x += en.speed * cos(en.angle)
        en.y += en.speed * sin(en.angle)
        if en.x < en.radius or en.x > width-en.radius:
            en.angle = PI-en.angle
        if en.y < en.radius or en.y > height-en.radius:
            en.angle *= -1
        noStroke()
        fill(en.color)
        ellipse(en.x,en.y,en.radius*2,en.radius*2)
