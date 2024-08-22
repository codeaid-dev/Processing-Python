def setup():
    size(500,500)

def draw():
    background(255)
    noStroke()
    fill(128,70,70)
    ellipse(width/2,height/2,width,height)
    leftX = width/2-100
    leftY = height/2
    rightX = width/2+100
    rightY = height/2
    followEye(leftX,leftY)
    followEye(rightX,rightY)

def followEye(x,y):
    fill(255)
    ellipse(x,y,100,100)
    angle = atan2(mouseY-y,mouseX-x)
    fill(0)
    ellipse(x+cos(angle)*20,
            y+sin(angle)*20,
            50,50)
