img = None
def setup():
    global img
    size(900,400)
    img = loadImage("panda.jpg")

def draw():
    pass

def mouseDragged():
    c = img.get(mouseX,mouseY)
    noStroke()
    fill(c)
    ellipse(mouseX,mouseY,20,20)

def mouseClicked():
    save("eyecatch.png")
