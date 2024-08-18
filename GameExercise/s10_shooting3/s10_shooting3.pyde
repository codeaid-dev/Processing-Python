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
    def draw(self,w=0,h=0):
        if w==0 or h==0:
            image(self.img,self.x,self.y)
        else:
            self.radius = h/2
            image(self.img,self.x,self.y,w,h)
    def collide(self,sprite):
        distance = sqrt((self.x-sprite.x)**2 + (self.y-sprite.y)**2)
        return distance < self.radius+sprite.radius

player = None
enemies = []
bullets = []
shoot = False
over = False
score = 0
def setup():
    global player
    size(600,800)
    imageMode(CENTER)
    player = Sprite(300,700,0,0,"player.png")

def draw():
    global shoot,over,score
    background(0)
    if over:
        textSize(50)
        textAlign(CENTER)
        text("GAME OVER\nSCORE: {}".format(score),
             316, 300)
        return

    if frameCount%30 == 0:
        enemies.append(Sprite(random(width),random(-500,-100),0,5,"ufo.png"))

    if keyPressed:
        if keyCode == UP:
            player.dy -= 1
        if keyCode == DOWN:
            player.dy += 1
        if keyCode == LEFT:
            player.dx -= 1
        if keyCode == RIGHT:
            player.dx += 1
            shoot = True
        if key == ' ' and shoot == False:
            b = Sprite(player.x,player.y,0,-5,"missiles.png")
            bullets.append(b)
            shoot = True
    else:
        shoot = False
    player.move(0.95)
    player.draw(60,40)
#    player.draw()
    for b in bullets:
        if b.y < -b.img.height/2:
            b.valid = False
            continue
        for e in enemies:
            if e.collide(b):
                score += 1
                b.valid = False
                e.valid = False
            if e.y > height+e.img.height/2:
                e.x = random(width)
                e.y = random(-500,-100)
    print('Enemies: '+str(len(enemies)))
    for e in list(enemies):
        if not e.valid:
            enemies.remove(e)
            continue
        e.move(1)
        e.draw(50,50)
#        e.draw()
        if e.collide(player):
            over = True
    print('Bullets: '+str(len(bullets)))
    for b in list(bullets):
        if not b.valid:
            bullets.remove(b)
            continue
        b.move(1)
        b.draw()
