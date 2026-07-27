def setup():
  size(600,300)

def draw():
  background(0);
  strokeWeight(2);
  for i in range(width/2+1):
    c = map(i,0,width/2,0,255)
    stroke(c)
    line(i*2,0,i*2,height)
