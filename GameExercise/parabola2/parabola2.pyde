x,y = 0,0
dx,dy = 0,0
gravity = 0.1
flying = False
angle = 60
speed = 10

def setup():
    global x,y
    size(500,500)
    x = 50
    y = height-25

def draw():
    global x,y,dx,dy,flying
    background(255)
    txt = 'angle: {}, speed: {}'.format(angle,speed)
    textSize(40)
    text(txt,50,50)
    fill(0)
    noStroke()
    ellipse(x,y,50,50)
    x += dx
    y += dy
    dy += gravity
    if y>=height-25:
        y = height-25
        dx *= 0.98
        if abs(dy) < 1.5:
            dy = 0
            flying = False
            if abs(dx) < 0.1:
                dx = 0
        else:
            dy *= -0.8
    if x<=25 or x>=width-25:
        dx *= -1
def keyPressed():
    global dx,dy,flying,angle,speed
    if key == ' ' and not flying:
        dx = speed*cos(radians(angle))
        dy = -speed*sin(radians(angle))
        flying = True
    if keyCode == UP:
        angle += 1
        if angle > 90:
            angle = 90
    if keyCode == DOWN:
        angle -= 1
        if angle < 0:
            angle = 0
    if keyCode == RIGHT:
        speed += 1
        if speed > 15:
            speed = 15
    if keyCode == LEFT:
        speed -= 1
        if speed < 1:
            speed = 1
