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
def setup():
    global player
    size(1000, 1000)
    player = Sprite("majo.png")
    player.x = width/2
    player.y = height/2
    player.angle = 0
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
