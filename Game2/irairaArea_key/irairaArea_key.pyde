class Circle:
    def __init__(self,x,y,s):
        self.x = x
        self.y = y
        self.s = s
        self.dx = 0
        self.dy = 0
        self.goal = False

    def display(self,c):
        fill(c)
        ellipse(self.x,self.y,self.s,self.s)

    def is_hit(self,obj):
        distance = dist(self.x,self.y,obj.x,obj.y)
        return distance<self.s/2+obj.s/2

player = None
walls = []
over,clear = False,False
timer = 400
up, down, left, right = False,False,False,False
def setup():
    global player
    size(600,400)
    player = Circle(60,60,30)
    goal = int(random(54))
    for i in range(54):
        x = i%9
        y = i/9
        c = color(255,0,0)
        w = Circle(x*66+34,y*66+34,30)
        if i == goal:
            w.goal = True
        walls.append(w)

def draw():
    global over,clear,timer
    background(255)
    noStroke()
    for w in walls:
        if w.goal:
            w.display(color(0,0,255))
        else:
            w.display(color(255,0,0))
    player.display(color(0))
    textSize(50)
    textAlign(CENTER)
    if over:
        text('GAME OVER',300,200)
        return
    if clear:
        text('CLEAR',300,200)
        return

    if keyPressed:
        if up:
            player.dy -= 0.1
        if down:
            player.dy += 0.1
        if left:
            player.dx -= 0.1
        if right:
            player.dx += 0.1

    player.dx *= 0.98
    player.dy *= 0.98
    player.x += player.dx
    player.y += player.dy

    for w in walls:
        if w.is_hit(player):
            if w.goal:
                clear = True
            else:
                over = True

    fill(255, 183, 0)
    rect(0, 0, 15, timer)
    timer -= 0.6
    if timer < 0:
        over = True

def keyPressed():
    global up, down, left, right
    if keyCode == UP:
        up = True
    if keyCode == DOWN:
        down = True
    if keyCode == LEFT:
        left = True
    if keyCode == RIGHT:
        right = True

def keyReleased():
    global up, down, left, right
    if keyCode == UP:
        up = False
    if keyCode == DOWN:
        down = False
    if keyCode == LEFT:
        left = False
    if keyCode == RIGHT:
        right = False
