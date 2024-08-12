class Circle:
    pass
circles = []
def setup():
    size(600,600)
    for i in range(10):
        c = Circle()
        c.radius = 15
        c.x = random(c.radius,width-c.radius)
        c.y = random(c.radius,height-c.radius)
        c.angle = random(TWO_PI)
        c.speed = random(2,6)
        c.iro = color(0,255,0)
        circles.append(c)

def draw():
    background(255)
    for c in circles:
        c.x += c.speed * cos(c.angle)
        c.y += c.speed * sin(c.angle)
        if c.x < c.radius or c.x > width-c.radius:
            c.angle = PI-c.angle
        if c.y < c.radius or c.y > height-c.radius:
            c.angle *= -1
        noStroke()
        fill(c.iro)
        ellipse(c.x,c.y,c.radius*2,c.radius*2)
