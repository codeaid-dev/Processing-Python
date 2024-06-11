class Snake:
    def __init__(self):
        self.body = [PVector(9,9) for i in range(5)]
        self.dx = 0
        self.dy = 0
    def direction(self,dx,dy):
        self.dx = dx
        self.dy = dy
    def move(self):
        for i in range(len(self.body)-1,0,-1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy
    def display(self):
        fill(0,255,0)
        for i in range(len(self.body)):
            rect(self.body[i].x*30,self.body[i].y*30,30,30)
    def collision(self):
        return self.body[0].x < 0 or \
            self.body[0].x > 19 or \
            self.body[0].y < 0 or \
            self.body[0].y > 19

snake = None
over = False

def setup():
    global snake
    frameRate(10)
    size(600,600)
    snake = Snake()

def draw():
    global over
    #background(0)
    stroke(64)
    fill(0)
    for y in range(20):
        for x in range(20):
            rect(x*30,y*30,30,30)
    if over:
        textAlign(CENTER)
        textSize(50)
        fill(255,0,0)
        text('Game Over', width/2,height/2)
        return
    snake.move()
    snake.display()
    if snake.collision():
        over = True

def keyPressed():
    if keyCode == UP:
        snake.direction(0,-1)
    if keyCode == DOWN:
        snake.direction(0,1)
    if keyCode == LEFT:
        snake.direction(-1,0)
    if keyCode == RIGHT:
        snake.direction(1,0)
