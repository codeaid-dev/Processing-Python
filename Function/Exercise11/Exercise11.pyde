x,y = 0,0
ox,oy = 0,0
status = False
def setup():
    global x,y
    size(500,500)
    x = width/2
    y = height/2

def draw():
    background(255)
    fill(0)
    ellipse(x,y,50,50)

def mousePressed():
    global status,ox,oy
    d = dist(mouseX,mouseY,x,y)
    if d < 25:
        ox = mouseX
        oy = mouseY
        status = True
    else:
        status = False

def mouseDragged():
    global x,y,ox,oy
    if status:
        mx = mouseX - ox
        my = mouseY - oy
        x += mx
        y += my
        ox = mouseX
        oy = mouseY
