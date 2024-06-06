class Circle:
    pass

def setup():
    global en
    size(500,500)
    en = Circle()
    en.x = width/2
    en.y = height/2
    en.sx = random(5)
    en.sy = random(5)
    en.r = 15
    en.sd = 1
    noStroke()

def draw():
    background(0)
    en.x += en.sx
    en.y += en.sy
    if en.x < en.r or en.x > width-en.r:
        en.sx *= -1
    if en.y < en.r or en.y > height-en.r:
        en.sy *= -1
    ellipse(en.x,en.y,en.r*2,en.r*2)
    
    if frameCount % 5 == 0:
        en.r += en.sd
        if en.r*2 <= 0 or en.r*2 > 100:
            en.sd *= -1
    
