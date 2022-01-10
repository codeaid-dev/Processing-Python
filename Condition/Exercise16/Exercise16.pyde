c1,c2 = 0,255
c1_change,c2_change = 1,-1

def setup():
    size(300,300)

def draw():
    global c1,c2,c1_change,c2_change
    noStroke()
    fill(c1,0,c2)
    rect(0,0,width/2,height)
    fill(c2,0,c1)
    rect(width/2,0,width/2,height)
    c1 = c1 + c1_change
    c2 = c2 + c2_change
    if c1<0 or c1>255:
        c1_change *= -1
    if c2<0 or c2>255:
        c2_change *= -1
