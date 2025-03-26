class Ball:
    def __init__(self):
        self.x,self.y = 250,300
        self.dx = random(-4,4)
        self.dy = random(2,4)
        self.s = 10
    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x < self.s/2 or self.x > width-self.s/2:
            self.dx *= -1
        if self.y < self.s/2 or self.y > height-self.s/2:
            self.dy *= -1
    def collision(self,brick):
        if self.x < brick.x:
            closestX = brick.x
        elif self.x > brick.x + brick.w:
            closestX = brick.x + brick.w
        else:
            closestX = self.x
    
        if self.y < brick.y:
            closestY = brick.y
        elif self.y > brick.y + brick.h:
            closestY = brick.y + brick.h
        else:
            closestY = self.y
        dx = self.x - closestX
        dy = self.y - closestY
        distance = sqrt(dx * dx + dy * dy)
        return distance < self.s/2
    def is_bottom(self):
        return self.y+self.s/2 > height


class Brick:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

ball = None
player = None
mode = 'stop' # stop:stop, play:playing, over:gameover, clear:gameclear
bricks = []

def setup():
    global player,ball
    size(500,600)
    ball = Ball()
    player = Brick(mouseX-25,570,50,20)
    colorMode(HSB)
    for i in range(30):
        x = 50+i%5*80
        y = 50+i//5*30
        b = Brick(x,y,80,30)
        b.c = color(i//5*40,255,255)
        bricks.append(b)
    colorMode(RGB)

def draw():
    global mode
    background(0)
    for b in bricks:
        fill(b.c)
        rect(b.x,b.y,b.w,b.h)
    if mode == 'play':
        ball.move()
    fill(255)
    ellipse(ball.x,ball.y,ball.s,ball.s)
    player.x = mouseX-25
    rect(player.x,player.y,player.w,player.h)

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
        dx = -4 + 8 * (ball.x-player.x)/player.w
        #dx = map(ball.x,player.x,player.x+player.w,-4,4)
        ball.dx = dx
        ball.dy = -abs(ball.dy)

    for b in bricks:
        if ball.collision(b):
            if ball.y-ball.s/2 < b.y+b.h < ball.y+ball.s/2 or \
                ball.y-ball.s/2 < b.y < ball.y+ball.s/2:
                ball.dy *= -1
            else:
                ball.dx *= -1
            bricks.remove(b)
            break

    if len(bricks) == 0:
        mode = 'clear'

    if ball.is_bottom():
        mode = 'over'

def keyPressed():
    global mode
    if key == ' ':
        if mode == 'stop':
            mode = 'play'
