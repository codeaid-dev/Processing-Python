player = PVector(60,60)
s = 30
speed = PVector(0,0)
wc = 54
wall = []

def setup():
    global wall
    size(600, 400)
    for i in range(wc):
        wall.append(PVector(s+(s*2+8)*(i%9),\
                             s+(s*2+8)*(i/9)))

def draw():
    global player,s,speed,wc,wall
    background(255)
    noStroke()
    for i in range(wc):
        fill(255, 0, 0)
        ellipse(wall[i].x, wall[i].y, s, s)
    fill(0)
    ellipse(player.x, player.y, s, s)

    if keyPressed:
        if keyCode == UP:
            speed.y -= 0.1
        if keyCode == DOWN:
            speed.y += 0.1
        if keyCode == LEFT:
            speed.x -= 0.1
        if keyCode == RIGHT:
            speed.x += 0.1

    speed.x *= 0.98
    speed.y *= 0.98
    player.x += speed.x
    player.y += speed.y
