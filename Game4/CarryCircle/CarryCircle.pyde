class Circle:
    pass

circles = []
complete = False
over = False
saved = 0
def setup():
    global x,y,saved
    size(500,500)
    textAlign(CENTER)
    textSize(50)
    for i in range(20):
        c = Circle()
        c.x = random(25,width-25)
        c.y = random(height/2+25,height-25)
        c.status = False
        circles.append(c)
    saved = millis()

def draw():
    global complete,over
    background(255)
    strokeWeight(3)
    line(0,height/2,width,height/2)
    count = 0
    for c in circles:
        fill(0)
        ellipse(c.x,c.y,50,50)
        if c.y < height/2:
            count += 1
    if count >= 20:
        complete = True

    fill(255,0,0)
    passed = (millis() - saved)/1000
    if (passed >= 20 and complete == False) or over:
        text('Time Over',width/2,height/2)
        over = True
    elif complete:
        text('Finish!',width/2,height/2)
    else:
        text(20-passed,width/2,height/2)

def mousePressed():
    for c in circles:
        d = dist(mouseX,mouseY,c.x,c.y)
        if d < 25:
            c.ox = mouseX
            c.oy = mouseY
            c.status = True
        else:
            c.status = False

def mouseDragged():
    for c in circles:
        if c.status:
            mx = mouseX - c.ox
            my = mouseY - c.oy
            c.x += mx
            c.y += my
            c.ox = mouseX
            c.oy = mouseY
