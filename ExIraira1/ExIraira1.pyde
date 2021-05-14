player = PVector(60,60)
s = 30
speed = PVector(0,0)

def setup():
    size(600, 400)

def draw():
    global player,s,speed
    background(255)
    noStroke()
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
