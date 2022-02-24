class Snow:
    def __init__(self,x,y,s):
        self.x=x
        self.y=y
        self.s=s

snows=[]
sekisetsu=[0 for i in range(200)]
def setup():
    size(800,600)
    for i in range(100):
        snows.append(Snow(random(width),random(height),random(1,6)))

def draw():
    background(0)
    noStroke()
    for snow in snows:
        snow.y+=snow.s/3
        if snow.y>height:
            snow.y=0
        okuyuki=snow.s/5
        fill(255,255*okuyuki)
        ellipse(snow.x,snow.y,snow.s,snow.s)

    for i,n in enumerate(sekisetsu):
        fill(255,200)
        ellipse(i*4, height, n*4, n*2)
    index = int(random(200))
    sekisetsu[index]+=1
        
