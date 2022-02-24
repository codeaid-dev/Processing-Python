x,y,s=[],[],[]
def setup():
    global x,y,s
    size(500,500)
    for i in range(200):
        x.append(random(width))
        y.append(random(height/2))
        s.append(random(0.1,2.0))

def draw():
    global x
    strokeWeight(2)
    for i in range(250):
        stroke(i)
        line(0,i*2,width,i*2)

    for i in range(len(x)):
        x[i]+=s[i]/20
        if x[i]>width:
            x[i]=0
        fill(255,255*s[i]/2)
        ellipse(x[i],y[i],s[i],s[i])
