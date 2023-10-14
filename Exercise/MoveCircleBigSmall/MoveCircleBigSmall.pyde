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
    en.dia = 30
    en.sd = 1
    noStroke()

def draw():
    background(0)
    en.x += en.sx
    en.y += en.sy
    if en.x < en.dia/2 or en.x > width-en.dia/2:
        en.sx *= -1
    if en.y < en.dia/2 or en.y > height-en.dia/2:
        en.sy *= -1
    ellipse(en.x,en.y,en.dia,en.dia)
    
    if frameCount % 5 == 0:
        en.dia += en.sd
        if en.dia <= 0 or en.dia > 100:
            en.sd *= -1
    
