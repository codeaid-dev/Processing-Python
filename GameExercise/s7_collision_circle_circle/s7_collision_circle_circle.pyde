class Circle:
    pass
circles = []
target = None
def setup():
    global target
    size(600,600)
    for i in range(10):
        c = Circle()
        c.radius = 15
        c.x = random(c.radius,width-c.radius)
        c.y = random(c.radius,height-c.radius)
        c.angle = random(TWO_PI)
        c.speed = random(2,6)
        c.iro = color(0,255,0)
        c.move = True
        circles.append(c)
    target = Circle()
    target.x = width/2
    target.y = height/2
    target.radius = 50

def draw():
    background(255)
    for c in circles:
        if c.move:
            c.x += c.speed * cos(c.angle)
            c.y += c.speed * sin(c.angle)
            if c.x < c.radius or c.x > width-c.radius:
                c.angle = PI-c.angle
            if c.y < c.radius or c.y > height-c.radius:
                c.angle *= -1
        distance = dist(c.x,c.y,target.x,target.y)
        if distance < (c.radius+target.radius)\
             or not c.move:
            fill(128)
            c.move = False
        else:
            fill(c.iro)
        noStroke()
        ellipse(c.x,c.y,c.radius*2,c.radius*2)
    fill(0)
    ellipse(target.x,target.y,
            target.radius*2,target.radius*2)
