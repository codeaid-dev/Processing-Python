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

class Brick:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

ball = None
player = None
mode = 'stop' # stop:stop, play:playing, over:gameover, clear:gameclear

def setup():
    global player,ball
    size(500,600)
    ball = Ball()
    player = Brick(mouseX-25,570,50,20)

def draw():
    background(0)
    if mode == 'play':
        ball.move()
    fill(255)
    ellipse(ball.x,ball.y,ball.s,ball.s)
    player.x = mouseX-25
    rect(player.x,player.y,player.w,player.h)

def keyPressed():
    global mode
    if key == ' ':
        if mode == 'stop':
            mode = 'play'
