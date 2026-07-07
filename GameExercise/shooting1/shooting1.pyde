class Sprite:
    def __init__(self,x,y,dx,dy,img):
        self.img = loadImage(img)
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = self.img.height/2
    def move(self,num):
        self.x += self.dx
        self.y += self.dy
        self.dx *= num
        self.dy *= num
    def draw(self):
        image(self.img,self.x,self.y)

player = None
up,down,left,right = False,False,False,False
def setup():
    global player
    size(600,800)
    imageMode(CENTER)
    player = Sprite(300,700,0,0,"player.png")

def draw():
    background(0)
    if keyPressed:
        if up:
            player.dy -= 1
        if down:
            player.dy += 1
        if left:
            player.dx -= 1
        if right:
            player.dx += 1
    player.move(0.95)
    player.draw()

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
