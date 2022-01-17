class Circle:
    def __init__(self,x,y,s):
        self.x = x
        self.y = y
        self.s = s
        self.dx = 0
        self.dy = 0

    def display(self,c):
        fill(c)
        ellipse(self.x,self.y,self.s,self.s)

player = None
def setup():
    global player,walls
    size(600,400)
    player = Circle(60,60,30)

def draw():
    background(255)
    noStroke()
    player.display(color(0))

    if keyPressed:
        if keyCode == LEFT:
            player.dx -= 0.1
        if keyCode == RIGHT:
            player.dx += 0.1
        if keyCode == UP:
            player.dy -= 0.1
        if keyCode == DOWN:
            player.dy += 0.1

    player.dx *= 0.98
    player.dy *= 0.98
    player.x += player.dx
    player.y += player.dy
