x,y=0,0
w,h=250,250
move=2
def setup():
    global x,y
    size(900, 300)
    x=width/2
    y=height/2

def draw():
    global x,move,w
    background(255)
    stroke(0)
    strokeWeight(300)
    rect(250,0,400,300)
    noStroke()
    fill(255,0,255)
    x += move
    if x>width/6*5:
        move *= -1
    if x<width/6:
        move *= -1
    if (move>0 and x>=width/2) or (move<0 and x<=width/2):
        w -= 1
    if (move<0 and x>=width/2) or (move>0 and x<=width/2):
        w += 1
    ellipse(x,y,w,h)
