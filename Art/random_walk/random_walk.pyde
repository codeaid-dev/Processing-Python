x = 250
y = 250
def setup():
    size(500,500)
    background(0)
    strokeWeight(5)

def draw():
    global x,y
    nextX = x + random(-5,5)
    nextY = y + random(-5,5)
    if nextX < 0:
        nextX = 0
    elif nextX > width:
        nextX = width
    
    if nextY < 0:
        nextY = 0
    elif nextY > height:
        nextY = height
    
    stroke(0,255,0,100)
    line(x,y,nextX,nextY)
    x = nextX
    y = nextY
