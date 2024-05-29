r=0
def setup():
    size(500,500)
    
def draw():
    global r
    background(0)
    stroke(255)
    pushMatrix()
    translate(width/2,height/2)
    r += 1
    rotate(radians(r))
    strokeWeight(2)
    line(0,0,0,height/2)
    popMatrix()
