class Circle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.w = 30
        self.sx = 0
        self.sy = 0
    def move(self,x,y):
        self.sx += x
        self.sy += y
        self.sx *= 0.98
        self.sy *= 0.98
        self.x += self.sx
        self.y += self.sy
    def collide_wall(self):
        return self.x<self.w/2 or \
        self.x>(width-self.w/2) or \
        self.y<self.w/2 or \
        self.y>(height-self.w/2)
    def collide_rect(self,rx,ry,rw,rh):
        return self.x+self.w/2 >= rx and \
        self.x-self.w/2 <= rx+rw and \
        self.y+self.w/2 >= ry and \
        self.y-self.w/2 <= ry+rh
    def display(self):
        fill(0)
        ellipse(self.x,self.y,self.w,self.w)

player = None
gameOver = False
r1,r2 = False,False

def setup():
    global player
    size(600, 400)
    player = Circle(width/2,height/2)

def draw():
    global gameOver, r1, r2
    background(255)
    fill(255)
    if player.collide_rect(50,50,100,100):
        r1 = True
    if r1:
        fill(255,0,0)
    else:
        fill(255)
    rect(50, 50, 100, 100)

    if player.collide_rect(450,250,100,100):
        r2 = True
    if r2:
        fill(0,0,255)
    else:
        fill(255)
    rect(450, 250, 100, 100)

    player.display()

    if r1 and r2:
        textSize(50)
        textAlign(CENTER)
        text("Succeed!", 300, 200)
        return
        
    if gameOver:
        textSize(50)
        textAlign(CENTER)
        text("Fail...", 300, 200)
        return

    if keyPressed:
        if keyCode == UP:
            player.move(0,-1)
        if keyCode == DOWN:
            player.move(0,1)
        if keyCode == LEFT:
            player.move(-1,0)
        if keyCode == RIGHT:
            player.move(1,0)

    player.move(0,0)

    if player.collide_wall():
        gameOver = True
