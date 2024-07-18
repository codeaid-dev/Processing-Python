centerX,centerY=0,0
def setup():
    global centerX,centerY
    size(500,500)
    centerX = width/2
    centerY = height/2

def draw():
    background(255)
    drawGuide()
    angle = atan2(mouseY-centerY, mouseX-centerX)
    x = centerX+200*cos(angle)
    y = centerY+200*sin(angle)
    angle = (angle+2*PI)%(2*PI)
    stroke(0)
    arc(centerX,centerY,50,50,0,angle,OPEN)
    showDegrees(angle)
    line(centerX,centerY,x,y)
    fill(0)
    ellipse(x,y,10,10)

def drawGuide():
    noFill()
    stroke(200)
    ellipse(centerX,centerY,400,400)
    line(centerX,centerY-200,centerX,centerY+200)
    line(centerX-200,centerY,centerX+200,centerY)

def showDegrees(r):
    d = degrees(r)
    textAlign(CENTER)
    textSize(20)
    text(str(ceil(d))+" degrees\n"+str(nf(r,1,2))+" radians",
        centerX,
        centerY+50)
