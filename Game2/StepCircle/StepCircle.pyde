class Step:
    def __init__(self,x,y,length,iro,pos):
        self.x = x
        self.y = y
        self.length = length
        self.iro = iro
        self.pos = pos
steps = []
x, y, g = 0, 0, 0
s = 30
sx, sy = 0, 0
over = False
clear = False
up, left, right = False,False,False

def setup():
    global x, y, g, w, h
    size(600, 400)
    x = 40
    y = 40
    g = 1
    s = 30
    for i in range(6):
        s_x = 10
        s_y = 350
        if i == 5:
            iro = color(255,0,0)
            pos = 'goal'
        else:
            iro = color(0,0,0)
            pos = 'step'
        step = Step(s_x+(i*100),s_y-(i*50),50,iro,pos)
        steps.append(step)

def draw():
    global x, y, sx, sy, g, over, clear
    background(255)

    stroke(0)
    strokeWeight(6)
    for step in steps:
        stroke(step.iro)
        line(step.x, step.y, step.x+step.length, step.y)

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

    for step in steps:
        if step.x <= x <= step.x+step.length and step.y >= y >= step.y-s/2:
            y = step.y-s/2
            g = 0
            if step.pos == 'goal':
                clear = True
                return
            break
    else:
        g += 0.1

    if keyPressed:
        if up and g == 0:
            sy -= 7
        if left:
            sx -= 0.1
        if right:
            sx += 0.1

    sx *= 0.98
    sy *= 0.98
    x += sx
    y += sy
    y += g

    if x < s/2 or x > (width - s/2) or y < s/2 or y > (height - s/2):
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
