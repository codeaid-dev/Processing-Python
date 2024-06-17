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

def collision(sx,sy,ex,ey,tx,ty,radius):
    StoC = PVector(tx-sx,ty-sy)
    EtoC = PVector(tx-ex,ty-ey)
    StoE = PVector(ex-sx,ey-sy)
    normalized_StoE = PVector(ex-sx,ey-sy)
    normalized_StoE.normalize()

    pj = StoC.x*normalized_StoE.y-normalized_StoE.x*StoC.y
    if abs(pj) < radius:
        dot1 = StoC.x*StoE.x
        dot2 = EtoC.x*StoE.x+EtoC.y*StoE.y
        if dot1 * dot2 <= 0.0:
            return True
        else:
            if dist(sx,sy,tx,ty)<radius or dist(ex,ey,tx,ty)<radius:
                return True
            else:
                return False
    else:
        return False
