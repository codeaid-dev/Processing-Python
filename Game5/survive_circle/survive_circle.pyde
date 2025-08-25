class Circle:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
        self.available = True

    def draw(self, c):
        noStroke()
        fill(c)
        ellipse(self.x, self.y, self.s, self.s)

    def follow(self, x, y):
        dx = x - self.x
        dy = y - self.y
        angle = atan2(dy, dx)
        distance = dist(self.x, self.y, x, y)
        
        if distance >= 1:
            self.x += cos(angle)
            self.y += sin(angle)

    def is_hit(self, obj):
        dst = dist(self.x,self.y,obj.x,obj.y)
        return dst < self.s/2 + obj.s/2

circles = []
player = None
bullets = []
over = False
score = 0

def setup():
    global player
    size(500, 1000)
    create_enemy()
    player = Circle(250, 950, 50)

def draw():
    global over, score
    background(255)
    textAlign(CENTER)
    textSize(50)
    fill(0)
    text('SCORE: '+str(score),250,50)
    if over:
        fill(255,0,0)
        text('GAME OVER',250,500)
        return

    if mouseX != 0 and mouseY != 0:
        player.x = mouseX
        player.y = mouseY
    player.draw(color(0,128,0))

    for c in circles:
        c.follow(player.x, player.y)
        if c.available and c.is_hit(player):
            over = True
            return
        if c.available:
            c.draw(color(0,255,0))

    for b in list(bullets):
        b.y -= 5
        for c in list(circles):
            if b.is_hit(c):
                b.available = False
                c.available = False
                score += 1
                break
        else:
            b.draw(color(255,0,0))
        if b.y < -b.s/2:
            b.available = False

    if frameCount % 120 == 0:
        create_enemy()

    delete_enemy()
    delete_bullet()

def create_enemy():
    for i in range(100):
        c = Circle(random(width),
                   random(-height, -50),
                   20)
        circles.append(c)

def delete_enemy():
    global circles
    circles = [c for c in circles if c.available]

def delete_bullet():
    global bullets
    bullets = [b for b in bullets if b.available]

def keyPressed():
    if key == ' ':
        b = Circle(player.x, player.y, 10)
        bullets.append(b)
    
