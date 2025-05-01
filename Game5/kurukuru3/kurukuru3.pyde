class Sprite:
    def __init__(self, file=None):
        if file is not None:
            self.img = loadImage(file)
        self.bullets = []
    def shot(self, speed):
        rad = radians(self.angle)
        b = Bullet(self.x, self.y, rad, speed)
        self.bullets.append(b)

class Bullet:
    def __init__(self, x, y, rad, speed):
        self.x = x
        self.y = y
        self.rad = rad
        self.speed = speed
    def move(self):
        self.x += self.speed * cos(self.rad)
        self.y += self.speed * sin(self.rad)
    def display(self, iro):
        noStroke()
        fill(iro)
        circle(self.x, self.y, 20)

player = None
shooting = False
monsters = []
score = 0
def setup():
    global player
    size(1000, 1000)
    player = Sprite("majo.png")
    if player.img.width <= player.img.height:
        player.r = player.img.width/2
    else:
        player.r = player.img.height/2
    player.x = width/2
    player.y = height/2
    player.angle = 0
    player.HP = 5
    for i in range(10):
        m = Sprite("monster"+str(i%4+1)+".png")
        if m.img.width <= m.img.height:
            m.r = m.img.width/2
        else:
            m.r = m.img.height/2
        m.angle = random(360)
        m.distance = width/2
        m.x = width/2 + m.distance*cos(radians(m.angle))
        m.y = height/2 + m.distance*sin(radians(m.angle))
        m.speed = random(1,3)
        m.apear = False
        monsters.append(m)
    imageMode(CENTER)
    textSize(50)
    textAlign(CENTER)

def draw():
    global shooting, score
    background(200)
    fill(0)
    text("SCORE: " + str(score) 
         + " HP: " + str(player.HP),
         width/2, 50)
    if player.HP <= 0:
        text("GAME OVER", width/2, height/2)
        return

    if keyPressed:
        if keyCode == LEFT:
            player.angle -= 3
        if keyCode == RIGHT:
            player.angle += 3
        if key == ' ' and shooting == False:
            player.shot(5)
            shooting = True
    else:
        shooting = False

    for b in player.bullets:
        b.move()
        b.display(color(255,255,0))

    pushMatrix()
    translate(width/2, height/2)
    rotate(radians(player.angle))
    image(player.img, 0, 0)
    popMatrix()

    if frameCount % 120 == 0:
        m = monsters[int(random(len(monsters)))]
        if m.apear == False:
            m.apear = True

    for m in monsters:
        hantei = dist(m.x,m.y,player.x,player.y)
        if m.apear:
            if hantei < m.r + player.r - 10:
                player.HP -= 1
                m.angle = random(360)
                m.distance = width/2
                m.x = width/2 + m.distance*cos(radians(m.angle))
                m.y = height/2 + m.distance*sin(radians(m.angle))
                m.speed = random(1,4)
                m.apear = False
            elif m.distance > 0:
                m.distance -= m.speed
                m.x = width/2 + m.distance*cos(radians(m.angle))
                m.y = height/2 + m.distance*sin(radians(m.angle))
                image(m.img, m.x, m.y)

        for b in list(player.bullets):
            hantei = dist(m.x,m.y,b.x,b.y)
            if hantei < 10+m.r:
                score += 1
                player.bullets.remove(b)
                m.angle = random(360)
                m.distance = width/2
                m.x = width/2 + m.distance*cos(radians(m.angle))
                m.y = height/2 + m.distance*sin(radians(m.angle))
                m.speed = random(1,4)
                m.apear = False
