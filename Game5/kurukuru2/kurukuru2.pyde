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
def setup():
    global player
    size(1000, 1000)
    player = Sprite("majo.png")
    player.x = width/2
    player.y = height/2
    player.angle = 0
    for i in range(10):
        m = Sprite("monster"+str(i%4+1)+".png")
        m.angle = random(360)
        m.distance = width/2
        m.x = width/2 + m.distance*cos(radians(m.angle))
        m.y = height/2 + m.distance*sin(radians(m.angle))
        m.speed = random(1,3)
        m.apear = False
        monsters.append(m)
    imageMode(CENTER)

def draw():
    global shooting
    background(200)
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
        if m.apear:
            if m.distance > 0:
                m.distance -= m.speed
                m.x = width/2 + m.distance*cos(radians(m.angle))
                m.y = height/2 + m.distance*sin(radians(m.angle))
                image(m.img, m.x, m.y)
            elif m.distance <= 0:
                m.angle = random(360)
                m.distance = width/2
                m.x = width/2 + m.distance*cos(radians(m.angle))
                m.y = height/2 + m.distance*sin(radians(m.angle))
                m.speed = random(1,4)
                m.apear = False
