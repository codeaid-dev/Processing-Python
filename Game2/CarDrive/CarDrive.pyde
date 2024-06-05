class Car:
    def __init__(self,x,y,c):
        self.x = x
        self.y = y
        self.c = c
        self.yspeed = random(1,6)

    def display(self):
        strokeWeight(8)
        line(self.x-10,self.y-20,self.x-10,self.y-5)
        line(self.x-10,self.y+5,self.x-10,self.y+20)
        line(self.x+10,self.y-20,self.x+10,self.y-5)
        line(self.x+10,self.y+5,self.x+10,self.y+20)
        strokeWeight(1)
        fill(self.c)
        ellipse(self.x,self.y,20,50)

    def move_x(self,mx):
        self.x += mx
        if self.x<=0 or self.x>=width:
            self.x += mx*-1

    def move_y(self,my=0):
        if my == 0:
            self.y += self.yspeed
        else:
            self.y += my

    def is_hit(self,obj):
        if self.x-10<obj.x+10 and self.x+10>obj.x-10 and \
        self.y-20<obj.y+20 and self.y+20>obj.y-20:
            return True
        else:
            return False

x,y = 150,200
car = None
cars = []
over = False
time = 0
def setup():
    global car
    size(300,400)
    car = Car(x,y,color(255))

def draw():
    global over,time
    background(200)
    car.display()
    if over:
        textSize(20)
        textAlign(CENTER)
        text('GAME OVER', width/2, 150)
        text('Time: '+str(time),width/2,180)
        return

    if frameCount % 50 == 0:
        pos = int(random(1,4))
        col = color(random(256),random(256),random(256))
        cars.append(Car(pos*width/4,25,col))

    for c in cars:
        c.move_y()
        c.display()
        if car.is_hit(c):
            time = frameCount/60
            over = True
            return

def keyPressed():
    if keyCode == LEFT:
        car.move_x(-width/4)
    if keyCode == RIGHT:
        car.move_x(width/4)
    if keyCode == UP:
        car.move_y(-20)
    if keyCode == DOWN:
        car.move_y(20)
