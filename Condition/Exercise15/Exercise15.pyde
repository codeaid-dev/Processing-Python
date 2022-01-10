x,y = 250,250
dx,dy = 2,3
def setup():
    size(500,500)

def draw():
    background(200)
    global x,y,dx,dy
    fill(255)
    x += dx
    y += dy
    if x-100<0 or x+100>width:
        dx *= -1
    if y-50<0 or y+50>height:
        dy *= -1
    draw_ufo(x,y)

def draw_ufo(x,y):
    strokeWeight(5)
    fill(255)
    ellipse(x-50,y+10,50,50)
    ellipse(x,y+20,50,50)
    ellipse(x+50,y+10,50,50)
    ellipse(x,y,200,50)
    ellipse(x,y-25,120,50)
