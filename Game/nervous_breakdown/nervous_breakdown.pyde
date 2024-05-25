colors=[color(255,0,0),color(0,255,0),color(0,0,255),color(255,255,0),
        color(255,0,255),color(0,255,255),color(0),color(128,0,0),color(128)]
tiles=[]
status=[0 for i in range(16)]
def setup():
    size(600,600)
    for i in range(16):
        while True:
            c=int(random(8))
            if 0<=tiles.count(c)<=1:
                tiles.append(c)
                break
    noStroke()

def draw():
    background(255)
    for i in range(16):
        if status[i]==0:
            fill(colors[8])
        else:
            fill(colors[tiles[i]])
        ellipse(i%4*150+75,i/4*150+75,150,150)

def mousePressed():
    for i in range(16):
        dst=dist(mouseX,mouseY,i%4*150+75,i/4*150+75)
        if dst<=75:
            status[i]=1
            break
