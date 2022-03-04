xpos, ypos = [],[]

def setup():
    size(500,500)
    for i in range(50):
        xpos.append(0)
        ypos.append(0)

def draw():
    background(255)
    for i in range(49):
        xpos[i] = xpos[i+1]
        ypos[i] = ypos[i+1]
    xpos[49] = mouseX
    ypos[49] = mouseY
    for i in range(50):
        noStroke()
        fill(255-i*5)
        ellipse(xpos[i],ypos[i],i,i)
