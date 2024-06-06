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
    global staus
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

def mousePressed():
    global status
    if status == 0:
        status = 1
