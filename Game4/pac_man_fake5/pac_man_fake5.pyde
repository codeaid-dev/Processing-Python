x,y = 300,300
up,down,left,right = False,False,False,False
dir = 1 #1:RIGHT,2:DOWN,3:LEFT,4:UP
open_mouse = True #True:open mouse,False:close mouse
move = False #True:moving,False:stoping

class Snack:
    pass
snacks = []

def setup():
    size(600,600)
    noStroke()
    for i in range(50):
        s = Snack()
        s.x = random(5,width-5)
        s.y = random(5,height-5)
        s.eat = False
        snacks.append(s)

def draw():
    global x,y,dir,open_mouse
    background(0)

    if keyPressed:
        move = True
        if up:
            y -= 5
            dir = 4
        if down:
            y += 5
            dir = 2
        if left:
            x -= 5
            dir = 3
        if right:
            x += 5
            dir = 1
    else:
        move = False

    for s in snacks:
        dst = dist(x,y,s.x,s.y)
        if dst<20:
            s.eat = True
        if not s.eat:
            fill(255,0,0)
            ellipse(s.x,s.y,10,10)

    if x<-15:
        x = width+15
    elif x>width+15:
        x = -15
    if y<-15:
        y = height+15
    elif y>height+15:
        y = -15

    if frameCount % 10 == 0:
        open_mouse = not open_mouse

    fill(255,255,0)
    if not move or open_mouse:
        if dir == 1:
            arc(x,y,30,30,radians(45),radians(315))
        elif dir == 2:
            arc(x,y,30,30,radians(135),radians(405))
        elif dir == 3:
            arc(x,y,30,30,radians(225),radians(495))
        else:
            arc(x,y,30,30,radians(315),radians(585))
    else:
        ellipse(x,y,30,30)

def keyPressed():
    global up,down,left,right
    if keyCode == UP:
        up = True
    if keyCode == DOWN:
        down = True
    if keyCode == LEFT:
        left = True
    if keyCode == RIGHT:
        right = True

def keyReleased():
    global up,down,left,right
    if keyCode == UP:
        up = False
    if keyCode == DOWN:
        down = False
    if keyCode == LEFT:
        left = False
    if keyCode == RIGHT:
        right = False
