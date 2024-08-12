rect_x,rect_y = 0,0
rect_yoko = 100
rect_tate = 50
circle_x,circle_y = 0,0
circle_s = 100
status = False
def setup():
    global rect_x,rect_y,circle_x,circle_y
    size(600,600)
    rect_x = width/2-rect_yoko/2
    rect_y = height-rect_tate*2
    circle_x = width/2
    circle_y = height/2

def draw():
    global circle_x,circle_y
    background(255)
    if status:
        fill(255,0,0)
        ellipse(mouseX,mouseY,
                circle_s,circle_s)
        circle_x = mouseX
        circle_y = mouseY
    else:
        fill(0,255,0)
        ellipse(circle_x,circle_y,
                circle_s,circle_s)

    fill(200)
    rect(rect_x,rect_y,rect_yoko,rect_tate)

def mousePressed():
    global status
    dst = dist(mouseX,mouseY,
               circle_x,circle_y)
    if dst<circle_s/2:
        status = not status

def keyPressed():
    global rect_x,rect_y
    if keyCode == UP:
        rect_y -= 10
    if keyCode == DOWN:
        rect_y += 10
    if keyCode == LEFT:
        rect_x -= 10
    if keyCode == RIGHT:
        rect_x += 10
