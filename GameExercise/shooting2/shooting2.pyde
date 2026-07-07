class Sprite:
    def __init__(self,x,y,dx,dy,img):
        self.img = loadImage(img)
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = self.img.height/2
        self.valid = True
    def move(self,num):
        self.x += self.dx
        self.y += self.dy
        self.dx *= num
        self.dy *= num
    def draw(self):
        image(self.img,self.x,self.y)
    def collide(self,sprite):
        distance = sqrt((self.x-sprite.x)**2 + (self.y-sprite.y)**2)
        return distance < self.radius+sprite.radius

player = None
up,down,left,right = False,False,False,False
enemies = []
bullets = []
shoot = False
def setup():
    global player
    size(600,800)
    imageMode(CENTER)
    player = Sprite(300,700,0,0,"player.png")

def draw():
    global shoot
    background(0)
    if frameCount%30 == 0:
        enemies.append(Sprite(random(width),random(-500,-100),0,5,"ufo.png"))

    if keyPressed:
        if up:
            player.dy -= 1
        if down:
            player.dy += 1
        if left:
            player.dx -= 1
        if right:
            player.dx += 1
        if key == ' ' and shoot == False:
            b = Sprite(player.x,player.y,0,-5,"missiles.png")
            bullets.append(b)
            shoot = True
    else:
        shoot = False
    player.move(0.95)
    player.draw()
    for b in bullets:
        for e in enemies:
            if e.collide(b):
                b.valid = False
                e.valid = False
    for e in list(enemies):
        if not e.valid:
            enemies.remove(e)
            continue
        e.move(1)
        e.draw()
    for b in list(bullets):
        if not b.valid:
            bullets.remove(b)
            continue
        b.move(1)
        b.draw()

def keyPressed():
    global up,down,left,right
    if keyCode == UP:
        up = True
    if keyCode == DOWN:
        down = True
    if keyCode == LEFT:
        left = True
    if keyCode == RIGHT:
        right = True

def keyReleased():
    global up,down,left,right
    if keyCode == UP:
        up = False
    if keyCode == DOWN:
        down = False
    if keyCode == LEFT:
        left = False
    if keyCode == RIGHT:
        right = False
