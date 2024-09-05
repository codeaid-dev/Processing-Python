def setup():
  size(600,600)
  noStroke()
  noLoop()

def draw():
  background(255)
  fill(0)
  for x in range(width):
    y = height/2+sin(x*0.01)*100
    ellipse(x,y,2,2)
