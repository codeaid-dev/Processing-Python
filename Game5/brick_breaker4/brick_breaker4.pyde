class Ball:
    def __init__(self):
        self.x,self.y = width/2,height/2
        self.radius = 5
        self.speed = 5
        # self.angle = random(QUARTER_PI,HALF_PI+ QUARTER_PI)
        self.angle = (PI/4)+random(1)*(PI/2)
        self.setAngle(random(45,135))
    def setAngle(self,deg):
        rad = deg * PI / 180
        self.dx = self.speed * cos(rad)
        self.dy = self.speed * sin(rad)
    def move(self):
        self.x += self.dx
        self.y += self.dy
        # self.x += self.speed*cos(self.angle)
        # self.y += self.speed*sin(self.angle)
        if self.x < self.radius or self.x > width-self.radius:
            self.dx *= -1
            # self.angle = PI-self.angle
        if self.y < self.radius or self.y > height-self.radius:
            self.dy *= -1
            # self.angle *= -1
    def draw(self):
        fill(255)
        ellipse(self.x,self.y,self.radius*2,self.radius*2)
    def collision(self,brick):
        if self.x < brick.x:
            closestX = brick.x
        elif self.x > brick.x+brick.w:
            closestX = brick.x+brick.w
        else:
            closestX = self.x
        if self.y < brick.y:
            closestY = brick.y
        elif self.y > brick.y+brick.h:
            closestY = brick.y+brick.h
        else:
            closestY = self.y
        distanceX = self.x-closestX
        distanceY = self.y-closestY
        distance = sqrt(distanceX*distanceX + distanceY*distanceY)
        return distance < self.radius
    def is_bottom(self):
        return self.y+self.radius > height

class Brick:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def draw(self):
        fill(self.c)
        rect(self.x,self.y,self.w,self.h)

ball = None
player = None
mode = 'stop' # stop:stop, play:playing, over:gameover, clear:gameclear
bricks = []

def setup():
    global player,ball
    size(600,800)
    ball = Ball()
    player = Brick(mouseX-25,770,50,20)
    player.c = color(255)
    colorMode(HSB)
    for i in range(30):
        x = 60+i%5*100
        y = 40+i//5*50
        b = Brick(x,y,80,30)
        b.c = color(i//5*40,255,255)
        bricks.append(b)
    colorMode(RGB)

def draw():
    global mode
    background(0)
    for brick in bricks:
        brick.draw()
    if mode == 'play':
        ball.move()
    ball.draw()
    player.x = mouseX-25
    player.draw()

    if mode == 'over':
        textAlign(CENTER)
        textSize(50)
        fill(255)
        text('GAME OVER',width/2,height/2)

    if mode == 'clear':
        textAlign(CENTER)
        textSize(50)
        fill(0,255,0)
        text('GAME CLEAR',width/2,height/2)

    if ball.collision(player):
        # 変換後の最小値+(変換後の範囲)*((指定した数値-変換前の最小値)/(変換前の範囲))
        center = player.x + player.w/2
        hitPos = (ball.x - center) / (player.w/2) # -1 ~ 1
        rad = hitPos * PI/3 # -60° ~ 60°
        ball.dx = ball.speed * sin(rad)
        ball.dy = -ball.speed * cos(rad)
        ball.y = player.y - ball.radius
        # ball.angle = PI+PI*(ball.x-player.x)/player.w
        #ball.angle = map(ball.x,player.x,player.x+player.w,PI,TWO_PI)

    for b in list(bricks):
        if ball.collision(b):
            if ball.y-ball.radius < b.y+b.h < ball.y+ball.radius or \
                ball.y-ball.radius < b.y < ball.y+ball.radius:
                ball.dy *= -1
                # ball.angle *= -1
            else:
                ball.dx *= -1
                # ball.angle = PI-ball.angle
            bricks.remove(b)

    if len(bricks) == 0:
        mode = 'clear'

    if ball.is_bottom():
        mode = 'over'

def keyPressed():
    global mode
    if key == ' ':
        if mode == 'stop':
            mode = 'play'
