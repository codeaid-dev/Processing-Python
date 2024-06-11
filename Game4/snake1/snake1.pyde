class Snake:
    def __init__(self):
        self.x = 9
        self.y = 9
        self.dx = 0
        self.dy = 0
        self.w = 30
    def direction(self,dx,dy):
        self.dx = dx
        self.dy = dy
    def move(self):
        self.x += self.dx
        self.y += self.dy
    def display(self):
        fill(0,255,0)
        rect(self.x*self.w,self.y*self.w,self.w,self.w)
    def collision(self):
        return self.x < self.w/2 or \
            self.x > width-self.w/2 or \
            self.y < self.w/2 or \
            self.y > height-self.w/2

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
        snake.direction(0,-2)
    if keyCode == DOWN:
        snake.direction(0,2)
    if keyCode == LEFT:
        snake.direction(-2,0)
    if keyCode == RIGHT:
        snake.direction(2,0)
