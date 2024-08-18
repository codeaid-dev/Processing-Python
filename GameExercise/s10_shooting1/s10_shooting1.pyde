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
def setup():
    global player
    size(600,800)
    imageMode(CENTER)
    player = Sprite(300,700,0,0,"player.png")

def draw():
    background(0)
    if keyPressed:
        if keyCode == UP:
            player.dy -= 1
        if keyCode == DOWN:
            player.dy += 1
        if keyCode == LEFT:
            player.dx -= 1
        if keyCode == RIGHT:
            player.dx += 1
    player.move(0.95)
    player.draw()
