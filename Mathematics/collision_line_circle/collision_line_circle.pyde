def setup():
    size(500,500)

def draw():
    background(200)
    x0 = 120
    y0 = 360
    x1 = 360
    y1 = 120
    x2 = mouseX
    y2 = mouseY
    radius = 50

    start_to_center = PVector(x2-x0,y2-y0)
    end_to_center = PVector(x2-x1,y2-y1)
    start_to_end = PVector(x1-x0,y1-y0)
    normal_start_to_end = PVector(x1-x0,y1-y0)
    normal_start_to_end.normalize()

    pj = start_to_center.x*normal_start_to_end.y-normal_start_to_end.x*start_to_center.y
    if abs(pj) < radius:
        dot1 = start_to_center.x*start_to_end.x
        dot2 = end_to_center.x*start_to_end.x+end_to_center.y*start_to_end.y
        if dot1 * dot2 <= 0.0:
            hit = True
        else:
            if dist(x0,y0,x2,y2)<radius or dist(x1,y1,x2,y2)<radius:
                hit = True
            else:
                hit = False
    else:
        hit = False

    strokeWeight(3)
    stroke(0)
    line(x0,y0,x1,y1)
    if hit:
        fill(255,0,0)
    else:
        fill(0,255,0)
    noStroke()
    ellipse(x2,y2,radius*2,radius*2)
