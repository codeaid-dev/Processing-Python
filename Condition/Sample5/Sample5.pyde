x,y=0,0
s=50
def setup():
    global x,y
    size(500,500)
    x = random(0,width-s)
    y = random(0,height-s)

def draw():
    global x,y
    background(255)
    if mouseX>x and mouseX<x+s and mouseY>y and mouseY<y+s:
        x = random(0,width-s)
        y = random(0,height-s)

    fill(0)
    rect(x,y,s,s)
    
