def setup():
    size(600,600)

def draw():
    r = 255.0 * mouseX / width
    b = 255.0 * mouseY / height
#    r = map(mouseX,0,width,0,255)
#    b = map(mouseY,0,height,0,255)
    background(r,0,b)
