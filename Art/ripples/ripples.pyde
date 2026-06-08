class Ripple:
    pass
rips = []

def setup():
    size(500,500)

def draw():
    noStroke()
    fill(0,10)
    rect(0,0,width,height)
    stroke(0,255,200)
    for rip in list(rips):
        if rip.r1 != 0:
            rip.r1+= 2
        if rip.r1 > 30 or rip.r2 != 0:
            rip.r2 += 2
        ellipse(rip.x,rip.y,rip.r1,rip.r1)
        ellipse(rip.x,rip.y,rip.r2,rip.r2)
        if rip.r1 > 100:
            rip.r1 = 0
        if rip.r2 > 100:
            rips.remove(rip)

def mousePressed():
    rip = Ripple()
    rip.x = mouseX
    rip.y = mouseY
    rip.r1 = 1
    rip.r2 = 0
    rips.append(rip)

def keyPressed():
    if key == ' ':
        save('ripples.png')
