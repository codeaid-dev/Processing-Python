r, g, b = 0, 0, 0
a, atari = 0, 0
hit = False

def setup():
    global r, g, b, a, atari
    size(700, 700)
    r = random(256)
    g = random(256)
    b = random(256)
    a = random(100, 250)
    atari = int(random(0, 100))

def draw():
    global hit
    background(255)
    noStroke()
    for i in range(100):
        if i == atari:
            fill(r, g, b, a)
        else:
            fill(r, g, b)
        x = 55 + 60 * (i % 10)
        y = 55 + 60 * (i / 10)
        rect(x, y, 50, 50)

    if hit:
        fill(0)
        textSize(32)
        textAlign(CENTER)
        text("Hit!!", width/2, 40)

    if mousePressed:
        atariX = 55 + 60 * (atari % 10)
        atariY = 55 + 60 * (atari / 10)
        if mouseX>atariX and mouseX<atariX+50 and \
            mouseY>atariY and mouseY<atariY+50:
            hit = True
