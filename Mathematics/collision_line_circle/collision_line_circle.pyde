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

    strokeWeight(3)
    stroke(0)
    line(Ax,Ay,Bx,By)
    if collision(Ax,Ay,Bx,By,Px,Py,radius):
        fill(255,0,0)
    else:
        fill(0,255,0)
    noStroke()
    ellipse(Px,Py,radius*2,radius*2)        

def collision(Ax,Ay,Bx,By,Px,Py,radius):
    AP = PVector(Px-Ax,Py-Ay)
    BP = PVector(Px-Bx,Py-By)
    AB = PVector(Bx-Ax,By-Ay)
    normalAB = PVector(Bx-Ax,By-Ay)
    normalAB.normalize()

    lenAX = normalAB.x*AP.x+normalAB.y*AP.y #単位ベクトルABとベクトルAPの内積(AXの距離)
    if lenAX < 0:
        shortest = dist(Ax,Ay,Px,Py) #AXが負ならAPが最短距離
    elif lenAX > dist(Ax,Ay,Bx,By):
        shortest = dist(Bx,By,Px,Py) #AXがABより長い場合はBPが最短距離
    else:
        lenPX = normalAB.x*AP.y-normalAB.y*AP.x #単位ベクトルAPとベクトルAPの外積(PXの距離)
        shortest = abs(lenPX) #PがAB線分上にあるので、PXが最短距離

    x = Ax+(normalAB.x*lenAX)
    y = Ay+(normalAB.y*lenAX)

    if shortest < radius:
        return True
    return False
