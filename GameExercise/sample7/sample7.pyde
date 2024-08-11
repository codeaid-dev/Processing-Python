class Circle:
    pass
circles = []
player = None
def setup():
    global player
    size(600,600)
    for i in range(10):
        en = Circle()
        en.x = width/2
        en.y = height/2
        en.angle = random(TWO_PI)
        en.speed = random(2,6)
        en.radius = 15
        en.iro = color(0,255,0)
        en.move = True
        circles.append(en)
    player = Circle()
    player.x = mouseX
    player.y = mouseY
    player.radius = 30

def draw():
    background(255)
    for en in circles:
        if en.move:
            en.x += en.speed * cos(en.angle)
            en.y += en.speed * sin(en.angle)
            if en.x < en.radius or en.x > width-en.radius:
                en.angle = PI-en.angle
            if en.y < en.radius or en.y > height-en.radius:
                en.angle *= -1
        distance = dist(en.x,en.y,player.x,player.y)
        if distance < (en.radius+player.radius) or not en.move:
            fill(128)
            en.move = False
        else:
            fill(en.iro)
        noStroke()
        ellipse(en.x,en.y,en.radius*2,en.radius*2)
    player.x = mouseX
    player.y = mouseY
    fill(0)
    ellipse(player.x,player.y,player.radius*2,player.radius*2)
