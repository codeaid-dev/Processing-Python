class Block:
    def __init__(self,x,y,w,h,t):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.type = t
    def display(self):
        if self.type == 'start':
            fill(255,255,0)
        elif self.type == 'wall':
            fill(255,0,0)
        elif self.type == 'goal':
            fill(0,0,255)
        noStroke()
        rect(self.x,self.y,self.w,self.h)

class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
    def move(self):
        self.dx *= 0.98
        self.x += self.dx
        self.y += self.dy
    def display(self):
        fill(0)
        noStroke()
        ellipse(self.x,self.y,30,30)
    def collision(self,b):
        if b.type == 'start':
            return b.x < self.x < b.x+b.w and \
                    b.y < self.y+15 < b.y+b.h
    def out_of_space(self):
        return 15 > self.x or self.x > width-15 or \
                15 > self.y or self.y > height-15

start = None
player = None

def setup():
    global start,player
    size(800,400)
    start = Block(50,300,50,30,'start')
    player = Player(75,280)

def draw():
    background(255)
    start.display()
    player.display()
    if player.collision(start):
        player.dy = 0
    else:
        player.dy += 0.1
    if keyPressed:
        if key == ' ':
            player.dy -= 0.2
        if keyCode == LEFT:
            player.dx -= 0.1
        if keyCode == RIGHT:
            player.dx += 0.1
    player.move()
    if player.out_of_space():
        player.x = 75
        player.y = 280
