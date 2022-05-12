class Circle:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def display(self):
        fill(self.color)
        ellipse(self.x,self.y,self.s,self.s)

player = None
enemy = []
status = 0
def setup():
    global player
    size(600,400)
    player = Circle(width/2,height/2)
    player.s = 20

def draw():
    global status
    background(0)
    if status == 0:
        fill(255)
        textAlign(CENTER)
        text("GAME START",width/2,height/2)
        return

    player.x = mouseX
    player.y = mouseY
    if status == 1:
        noStroke()
        player.color = color(255)
        player.display()

    if status == 2:
        fill(255)
        textAlign(CENTER)
        text("GAME OVER",width/2,height/2)
        return

    if frameCount%30 == 0:
        create_enemy()
    
    for e in enemy:
        if e.active:
            e.x += e.speed
            e.display()
            if is_hit(player.x,player.y,player.s,e.x,e.y,e.s):
                if player.s > e.s:
                    player.s += e.s * 0.1
                    e.active = False
                else:
                    status = 2

def mousePressed():
    global status
    if status == 0:
        status = 1

def create_enemy():
    e = Circle(0,random(0,height))
    e.speed = random(-3,4)
    if e.speed < 0:
        e.x = width
    e.s = random(player.s*0.5,player.s*2)
    e.color = color(random(256),random(256),random(256))
    e.active = True
    enemy.append(e)

def is_hit(px,py,ps,ex,ey,es):
    d = dist(px,py,ex,ey)
    return d < ps/2+es/2
