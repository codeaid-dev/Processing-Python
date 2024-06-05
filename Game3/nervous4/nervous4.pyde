colors=[color(255,0,0),color(0,255,0),
        color(0,0,255),color(255,255,0),
        color(255,0,255),color(0,255,255),
        color(0),color(128,0,0),color(128)]
tiles=[]
status=[0 for i in range(16)]
one,two=None,None
showCount=0
def setup():
    size(600,600)
    noStroke()
    for i in range(16):
        while True:
            c=int(random(8))
            if 0<=tiles.count(c)<=1:
                tiles.append(c)
                break

def draw():
    global showCount,one,two
    background(255)
    if one!=None and two!=None:
        if showCount<120:
            showCount+=1
        else:
            if tiles[one]!=tiles[two]:
                status[one]=0
                status[two]=0
            one=None
            two=None
            showCount=0
    for i in range(16):
        if status[i]==0:
            fill(colors[8])
        else:
            fill(colors[tiles[i]])
        ellipse(i%4*150+75,i/4*150+75,150,150)

def mousePressed():
    global one,two
    if one==None or two==None:
        for i in range(16):
            dst=dist(mouseX,mouseY,i%4*150+75,i/4*150+75)
            if dst<=75:
                if one==None:
                    one=i
                elif two==None:
                    two=i
                status[i]=1
                break
