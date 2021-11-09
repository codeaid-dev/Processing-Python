player = None
enemy = []
count = 0
status = 0
class Circle:
    pass

def setup():
    global player, enemy
    size(600,400)
    player = Circle()
    player.size = 20
    for i in range(100):
        en = Circle()
        en.active = False
        enemy.append(en)

def draw():
    global player, status, count
    background(0)
    if status == 0:
        fill(255)
        textAlign(CENTER)
        text("GAME START",width/2,height/2)
        return

    player.x = mouseX
    player.y = mouseY
    for en in enemy:
        if en.active == True:
            en.x += en.speed
            if isHit(player.x, player.y, player.size,
                         en.x, en.y, en.size):
                if player.size > en.size:
                    player.size += en.size * 0.1
                    en.active = False
                else:
                    status = 2
            noStroke()
            fill(en.color)
            ellipse(en.x, en.y, en.size, en.size)

    if status == 1:
        noStroke()
        fill(255)
        ellipse(player.x, player.y, player.size, player.size)
    if status == 2:
        fill(255)
        textAlign(CENTER)
        text("GAME OVER", width/2, height/2)
    count += 1
    if count % 30 == 0:
        create_enemy()

def create_enemy():
    for en in enemy:
        if en.active == False:
            en.speed = random(-3,4)
            if en.speed < 0:
                en.x = width
            else:
                en.x = 0
            en.y = random(0,height)
            en.size = random(player.size * 0.5, player.size * 2)
            en.color = color(random(256),random(256),random(256))
            en.active = True
            break

def mousePressed():
    global status
    if status == 0:
        status = 1
    if status == 2:
        status = 0

def isHit(px, py, ps, ex, ey, es):
    distance = dist(px, py, ex, ey)
    if distance < ps/2+es/2:
        return True
    return False
