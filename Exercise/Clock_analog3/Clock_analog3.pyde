def setup():
    size(500,500)

def draw():
    background(0)

    margin = 20
    fill(200)
    noStroke()
    for i in range(60):
        x = width/2 + (width/2-margin) * cos(radians(i*6))
        y = height/2 + (width/2-margin) * sin(radians(i*6))
        ellipse(x,y,5,5)
    for i in range(12):
        x = width/2 + (width/2-margin) * cos(radians(i*30))
        y = height/2 + (width/2-margin) * sin(radians(i*30))
        ellipse(x,y,20,20)
    
    stroke(255)
    s = second()
    m = minute() + (s/60.0)
    h = hour()%12 + (m/60.0)

    translate(width/2,height/2)
    rotate(radians(180))

    # Hour
    pushMatrix()
    rotate(radians(h*360/12))
    strokeWeight(5)
    line(0,0,0,height/3-margin)
    popMatrix()

    # Minute
    pushMatrix()
    rotate(radians(m*360/60))
    strokeWeight(3)
    line(0,0,0,height/2-margin)
    popMatrix()

    # Second
    pushMatrix()
    rotate(radians(s*360/60))
    strokeWeight(1)
    line(0,0,0,height/2-margin)
    popMatrix()
