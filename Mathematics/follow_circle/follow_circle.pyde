centerX,centerY=0,0
followX,followY=450,450
def setup():
    global centerX,centerY
    size(500,500)
    centerX = width/2
    centerY = height/2

def draw():
    background(255)
    fill(0)
    ellipse(mouseX,mouseY,10,10)

    drawSinCos(mouseX,mouseY)
    followCircle()

def drawSinCos(x,y):
    strokeWeight(1)
    stroke(0)
    line(followX,followY,x,y)
    stroke(0,200,0)
    line(followX,followY,followX,y)
    strokeWeight(5)
    point(followX,y)
    strokeWeight(1)
    stroke(255,175,0)
    line(followX,followY,x,followY)
    strokeWeight(5)
    point(x,followY)

def showDegrees(angle):
    angle = (angle+2*PI)%(2*PI)
    fill(0)
    textSize(30)
    textAlign(CENTER)
    text(str(ceil(degrees(angle)))+" degrees",
         centerX,height-100)
    text(str(int(angle*100)/100.0)+" radians",
         centerX,height-50)

def followCircle():
    global followX,followY
    dx = mouseX - followX
    dy = mouseY - followY
    angle = atan2(dy,dx)
    distance = dist(followX,followY,
                    mouseX,mouseY)
    if distance >= 1:
        followX += cos(angle)*2
        followY += sin(angle)*2
    noStroke()
    fill(255,0,0)
    ellipse(followX,followY,20,20)
    showDegrees(angle)
