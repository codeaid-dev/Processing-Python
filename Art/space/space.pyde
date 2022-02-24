x,y,s=[],[],[]
count=100
def setup():
    global x,y,s
    size(600,400)
    for i in range(count):
        x.append(random(width))
        y.append(random(height))
        s.append(random(1,6))

def draw():
    background(0)
    for i in range(count):
        x[i]+=s[i]
        if x[i]>width:
            x[i]=0
        noStroke()
        fill(255, 255*s[i]/6)
        ellipse(x[i],y[i],s[i],s[i])
