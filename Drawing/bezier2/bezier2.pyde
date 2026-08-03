class ControlPoint:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.drag = False
cp1,cp2,cp3 = None,None,None

t = 0
speed = 0.005

curve = []

def setup():
    global cp1,cp2,cp3
    size(500,500)
    cp1 = ControlPoint(50,450)
    cp2 = ControlPoint(250,50)
    cp3 = ControlPoint(450,450)

    textSize(20)
    textAlign(CENTER)

def draw():
    global t
    background(255)
    stroke(255,180,0)
    line(cp1.x,cp1.y,cp2.x,cp2.y)
    line(cp2.x,cp2.y,cp3.x,cp3.y)
    fill(255)
    circle(cp1.x,cp1.y,10)
    circle(cp2.x,cp2.y,10)
    circle(cp3.x,cp3.y,10)
    fill(0)
    text("1",cp1.x,cp1.y-10)
    text("2",cp2.x,cp2.y-10)
    text("3",cp3.x,cp3.y-10)
    fill(255)
    stroke(0)
    bezier(cp1.x,cp1.y,
        cp2.x,cp2.y,
        cp2.x,cp2.y,
        cp3.x,cp3.y)
    # 制御点1,2,3の補間
    ax = lerp(cp1.x, cp2.x, t)
    ay = lerp(cp1.y, cp2.y, t)
    bx = lerp(cp2.x, cp3.x, t)
    by = lerp(cp2.y, cp3.y, t)
    cx = lerp(ax, bx, t)
    cy = lerp(ay, by, t)

    # 補間線
    stroke(128)
    line(ax,ay,bx,by)
    # 補間点
    noStroke()
    fill(255,0,0)
    circle(ax,ay,10)
    fill(0,0,255)
    circle(bx,by,10)
    fill(0,255,0)
    circle(cx,cy,10)
    fill(0)
    text(t,cx,cy-10)
    
    # ベジェ曲線
    curve.append(ControlPoint(cx, cy))
    noFill()
    stroke(0,255,0)
    beginShape()
    for p in curve:
        vertex(p.x, p.y)
    endShape()

    t += speed
    if t > 1:
        t = 0
        curve[:] = []

def mousePressed():
    dst1 = dist(cp1.x,cp1.y,mouseX,mouseY)
    dst2 = dist(cp2.x,cp2.y,mouseX,mouseY)
    dst3 = dist(cp3.x,cp3.y,mouseX,mouseY)
    cp1.drag = False
    cp2.drag = False
    cp3.drag = False
    if dst3<=5: cp3.drag = True
    elif dst2<=5: cp2.drag = True
    elif dst1<=5: cp1.drag = True

def mouseDragged():
    mx = mouseX-pmouseX
    my = mouseY-pmouseY
    if cp1.drag:
        cp1.x += mx
        cp1.y += my
    if cp2.drag:
        cp2.x += mx
        cp2.y += my
    if cp3.drag:
        cp3.x += mx
        cp3.y += my
