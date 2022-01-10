x,y = 50,50
button = False

def setup():
    size(300,300)
    strokeWeight(5)

def draw():
    if button:
        background(255)
        stroke(0)
    else:
        background(0)
        stroke(255)
    fill(128)
    rect(x,y,200,100)

def mousePressed():
    global button
    if mouseX>x and mouseX<x+200 and \
        mouseY>y and mouseY<y+100:
        button = not button
