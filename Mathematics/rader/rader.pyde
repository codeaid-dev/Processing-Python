r = 0
targets = [[random(50,450),random(50,450),random(10,30)],
           [random(50,450),random(50,450),random(10,30)],
           [random(50,450),random(50,450),random(10,30)]]
def setup():
    size(500,500)

def draw():
    global r
    noStroke()
    fill(0,10)
    rect(0,0,width,height)
    ex = width/2 + width/2 * cos(radians(r))
    ey = height/2 + height/2 * sin(radians(r))
    stroke(0,255,0)
    strokeWeight(5)
    line(width/2,height/2,ex,ey)
    r += 1
    for t in targets:
        if collision(width/2,height/2,ex,ey,t[0],t[1],t[2]):
            fill(255)
            noStroke()
            ellipse(t[0],t[1],t[2]*2,t[2]*2)

def collision(Ax,Ay,Bx,By,Px,Py,radius):
    AP = PVector(Px-Ax,Py-Ay)
    BP = PVector(Px-Bx,Py-By)
    AB = PVector(Bx-Ax,By-Ay)
    normalAB = PVector(Bx-Ax,By-Ay)
    normalAB.normalize()

    #単位ベクトルABとベクトルAPの内積(AXの距離)
    lenAX = normalAB.x*AP.x+normalAB.y*AP.y
    if lenAX < 0:
        #AXが負ならAPが最短距離
        shortest = dist(Ax,Ay,Px,Py)
    elif lenAX > dist(Ax,Ay,Bx,By):
        #AXがABより長い場合はBPが最短距離
        shortest = dist(Bx,By,Px,Py)
    else:
        #単位ベクトルAPとベクトルAPの外積(PXの距離)
        lenPX = normalAB.x*AP.y-normalAB.y*AP.x
        #PがAB線分上にあるので、PXが最短距離
        shortest = abs(lenPX)

    if shortest < radius:
        return True
    return False
