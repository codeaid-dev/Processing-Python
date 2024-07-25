r=0
targets = [[random(50,450),random(50,450),random(10,100)],
           [random(50,450),random(50,450),random(10,100)],
           [random(50,450),random(50,450),random(10,100)]]
def setup():
    size(500,500)

def draw():
    global r
    noStroke()
    fill(0,10)
    rect(0,0,width,height)
    stroke(0,255,0)
    x = width/2 + width/2 * cos(radians(r))
    y = height/2 + height/2 * sin(radians(r))
    strokeWeight(5)
    line(x,y,width/2,height/2)
    r += 1
    for t in targets:
        if collision(x,y,width/2,height/2,t[0],t[1],t[2]/2):
            fill(0,255,0)
            ellipse(t[0],t[1],t[2],t[2])

def collision(Ax,Ay,Bx,By,Px,Py,radius):
    AP = PVector(Px-Ax,Py-Ay)
    AB = PVector(Bx-Ax,By-Ay)
    AB.normalize()

    #単位ベクトルABとベクトルAPの内積(AXの距離)
    lenAX = AB.x*AP.x+AB.y*AP.y
    if lenAX < 0:
        #AXが負ならAPが最短距離
        shortest = dist(Ax,Ay,Px,Py)
    elif lenAX > dist(Ax,Ay,Bx,By):
        #AXがABより長い場合はBPが最短距離
        shortest = dist(Bx,By,Px,Py)
    else:
        #単位ベクトルAPとベクトルAPの外積(PXの距離)
        lenPX = AB.x*AP.y-AB.y*AP.x
        #PがAB線分上にあるので、PXが最短距離
        shortest = abs(lenPX)

    if shortest < radius:
        return True
    return False
