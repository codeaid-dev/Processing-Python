crossPoint = PVector()

def setup():
    size(500,500)

def draw():
    background(200)
    Ax = 150
    Ay = 350
    Bx = 350
    By = 150
    Px = mouseX
    Py = mouseY
    radius = 50
    hit = False

    strokeWeight(3)
    stroke(0)
    line(Ax,Ay,Bx,By)
    if collision(Ax,Ay,Bx,By,Px,Py,radius):
        hit = True
        fill(255,0,0)
    else:
        fill(0,255,0)
    noStroke()
    ellipse(Px,Py,radius*2,radius*2)        
    if hit:
        fill(255,255,0)
        ellipse(crossPoint.x,crossPoint.y,10,10)

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

    crossPoint.x = Ax+(AB.x*lenAX)
    crossPoint.y = Ay+(AB.y*lenAX)

    if shortest < radius:
        return True
    return False
