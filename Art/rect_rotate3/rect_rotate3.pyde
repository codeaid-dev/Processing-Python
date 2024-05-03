x = 300
y = 200
angle = 0
speed = 1
rad = radians(angle)
def setup():
    size(600,400)

def draw():
    global rad,angle,speed
    background(0)
    fill(255)
    rectMode(CENTER)
    translate(x,y)
    angle += speed
    if angle>90 or angle<-90:
        speed *= -1
    rad += radians(speed)
    rotate(rad)
    rect(0,0,50,50)
