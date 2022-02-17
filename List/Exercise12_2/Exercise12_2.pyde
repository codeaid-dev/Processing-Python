px,py = 0,0
psize = 20
count = 0
ex,ey = [],[]
esize,espeed = [],[]
active = []
def setup():
    size(600,400)

def draw():
    global px,py,count
    background(0)
    px = mouseX
    py = mouseY    
    noStroke()
    fill(255)
    ellipse(px,py,psize,psize)

    count+=1
    if count%60 == 0:
        create()

    for i in range(len(active)):
        if active[i]:
            ex[i] += espeed[i]
            if ex[i]<0 or ex[i]>width:
                espeed[i]*=-1
            noStroke()
            fill(255,0,0)
            ellipse(ex[i],ey[i],esize[i],esize[i])

def create():
    speed = int(random(-3,4))
    if speed == 0:
        speed = 1
    espeed.append(speed)
    if speed < 0:
        ex.append(width)
    else:
        ex.append(0)
    ey.append(random(0,height))
    esize.append(random(psize*0.5, psize*2))
    active.append(True)
