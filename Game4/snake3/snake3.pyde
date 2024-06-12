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
        for i in range(1,len(self.body)):
            if (self.dx != 0 or self.dy != 0) and \
                self.body[0].x == self.body[i].x and \
                self.body[0].y == self.body[i].y:
                return True
        return self.body[0].x < 0 or \
            self.body[0].x > 19 or \
            self.body[0].y < 0 or \
            self.body[0].y > 19
    def add_body(self):
        pv = PVector(self.body[-1].x,self.body[-1].y)
        self.body.append(pv)
    def eat(self,food):
        return self.body[0].dist(food) == 0

class Food:
    def display(self):
        fill(255,0,0)
        rect(self.x*30,self.y*30,30,30)
    def set_position(self):
        self.x = int(random(19))
        self.y = int(random(19))

snake = None
food = None
over = False

def setup():
    global snake,food
    frameRate(10)
    size(600,600)
    snake = Snake()
    food = Food()
    food.set_position()

def draw():
    global over
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
    food.display()
    snake.move()
    snake.display()
    if snake.collision():
        over = True
    if snake.eat(PVector(food.x,food.y)):
        snake.add_body()
        food.set_position()

def keyPressed():
    if keyCode == UP:
        snake.direction(0,-1)
    if keyCode == DOWN:
        snake.direction(0,1)
    if keyCode == LEFT:
        snake.direction(-1,0)
    if keyCode == RIGHT:
        snake.direction(1,0)
