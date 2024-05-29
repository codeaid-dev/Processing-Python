def setup():
    size(500,500)

def draw():
    background(0)
    stroke(255)
    h = hour()%12
    m = minute()
    s = second()

    translate(width/2,height/2)
    rotate(radians(180))

    # Hour
    pushMatrix()
    rotate(radians(h*360/12))
    strokeWeight(5)
    line(0,0,0,height/3)
    popMatrix()

    # Minute
    pushMatrix()
    rotate(radians(m*360/60))
    strokeWeight(3)
    line(0,0,0,height/2)
    popMatrix()

    # Second
    pushMatrix()
    rotate(radians(s*360/60))
    strokeWeight(1)
    line(0,0,0,height/2)
    popMatrix()
