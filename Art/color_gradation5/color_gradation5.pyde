def setup():
    size(500,500)
    noStroke()

def draw():
    background(255)
    f = color(0);
    t = color(255);
    for i in range(width,0,-1):
        amt = map(i,0,width,0.0,1.0);
        c = lerpColor(f,t,amt);
        fill(c);
        ellipse(width/2,height/2,i,i);
