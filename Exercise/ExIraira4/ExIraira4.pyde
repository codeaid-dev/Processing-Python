player = PVector(60,60)
s = 30
speed = PVector(0,0)
wc = 54
wall = []
over = False

def setup():
    global wall
    size(600, 400)
    for i in range(wc):
        wall.append(PVector(s+(s*2+8)*(i%9),\
                             s+(s*2+8)*(i/9)))

def draw():
    global player,s,speed,wc,wall,over
    background(255)
    noStroke()
    for i in range(wc):
        fill(255, 0, 0)
        ellipse(wall[i].x, wall[i].y, s, s)
    fill(0)
    ellipse(player.x, player.y, s, s)

    if over:
        textSize(50)
        textAlign(CENTER)
        text("GAME OVER", 300, 200)
        return

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

    if player.x<s/2 or player.x>(width-s/2) \
    or player.y<s/2 or player.y>(height-s/2):
        over = True

    for i in range(wc):
        check = isHit(player.x, player.y, s,\
                       wall[i].x, wall[i].y, s)
        if check == 1:
            over = True

def isHit(px, py, ps, ex, ey, es):
    distance = dist(px, py, ex, ey)
    if distance < ps/2+es/2:
        return 1
    return 0
