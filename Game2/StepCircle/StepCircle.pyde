class Line:
    def __init__(self,x,y,length):
        self.x = x
        self.y = y
        self.length = length
        self.goal = False
    def draw(self):
        if self.goal:
            stroke(255,0,0)
        else:
            stroke(0)
        strokeWeight(6)
        line(self.x,
             self.y,
             self.x+self.length,
             self.y)
    def is_hit(self,x,y,radius):
        return self.x <= x <= self.x+self.length and \
        self.y >= y >= self.y-radius
lines = []
x, y = 40, 40
s = 30
dx, dy = 0, 0
over = False
clear = False
up, left, right = False,False,False
onGround = False

def setup():
    size(600, 400)
    for i in range(6):
        l = Line(i*100+10,350-i*50,50)
        if i == 5:
            l.goal = True
        lines.append(l)

def draw():
    global x, y, dx, dy, over, clear, onGround
    background(255)

    for l in lines:
        l.draw()

    noStroke()
    fill(0)
    ellipse(x, y, s, s)

    if over:
        textSize(50)
        textAlign(CENTER)
        text("GAME OVER", 300, 200)
        return

    if clear:
        textSize(50)
        textAlign(CENTER)
        text("CLEAR", 300, 200)
        return

    onGround = False
    for l in lines:
        if l.is_hit(x,y,s/2):
            dy = 0
            if l.goal:
                clear = True
            onGround = True
            break

    if keyPressed:
        if up and dy == 0:
            dy -= 7
        if left:
            dx -= 0.1
        if right:
            dx += 0.1

    dx *= 0.98
    dy *= 0.98
    x += dx
    y += dy

    if not onGround:
        dy += 0.3
    if y > (height - s/2):
        over = True

def keyPressed():
    global up, left, right
    if keyCode == UP:
        up = True
    if keyCode == LEFT:
        left = True
    if keyCode == RIGHT:
        right = True

def keyReleased():
    global up, left, right
    if keyCode == UP:
        up = False
    if keyCode == LEFT:
        left = False
    if keyCode == RIGHT:
        right = False
