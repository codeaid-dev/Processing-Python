class Sprite:
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.size = size
        self.valid = True
    def move_x(self,speed):
        self.x += speed
    def move_y(self,speed):
        self.y += speed
    def is_hit(self, sprite):
        dst = dist(sprite.x,sprite.y,self.x,self.y)
        return dst < (sprite.size+self.size)/2

ship = None
targets = []
bullets = []
shoot = False
over = False
time = ''
def setup():
    global ship
    size(500,800)
    noStroke()
    ship = Sprite(250,770,50)

def draw():
    global ship,targets,bullets,shoot,over,time
    background(255)

    if over:
        textSize(50)
        textAlign(CENTER)
        fill(255,0,0)
        text('GAME OVER', width/2, 300)
        text(time + ' sec',width/2,360)
        return
    else:
        time = str(int(frameCount/60))

    if frameCount % 10 == 0:
        t = Sprite(random(width),0,random(10,50))
        targets.append(t)

    if keyPressed:
        if keyCode == RIGHT:
            ship.move_x(3)
        if keyCode == LEFT:
            ship.move_x(-3)
        if keyCode == UP:
            ship.move_y(-3)
        if keyCode == DOWN:
            ship.move_y(3)
        if key == ' ' and shoot == False:
            b = Sprite(ship.x,ship.y,10)
            bullets.append(b)
            shoot = True
    else:
        shoot = False

    if ship.x < ship.size/2:
        ship.move_x(3)
    if ship.x > width-ship.size/2:
        ship.move_x(-3)
    if ship.y < ship.size/2:
        ship.move_y(3)
    if ship.y > height-ship.size/2:
        ship.move_y(-3)

    fill(0,0,255)
    ellipse(ship.x,ship.y,ship.size,ship.size)

    for b in bullets:
        b.move_y(-5)
        fill(255 ,0,0)
        ellipse(b.x,b.y,b.size,b.size)

    for t in targets:
        t.move_y(5)
        fill(0)
        ellipse(t.x,t.y,t.size,t.size)
        if t.is_hit(ship):
            over = True

    for b in bullets:
        for t in targets:
            if t.is_hit(b):
                b.valid = False
                t.valid = False
    bullets = [b for b in bullets if b.valid]
    targets = [t for t in targets if t.valid]
    
