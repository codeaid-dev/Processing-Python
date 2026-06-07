def setup():
  size(500,500)
  rectMode(CENTER)

def draw():
  background(255)
  stroke(0,155,155)
  for y in range(9):
    for x in range(9):
      if (y%2==0 and x%2!=0) \
          or (y%2!=0 and x%2==0):
        fill(255)
        ellipse(30+x*55,30+y*55,50,50)
      elif (y%2==0 and x%2==0) \
          or (y%2!=0 and x%2!=0):
        if y==4 or x==4:
          fill(255,0,0)
        else:
          fill(255)
        rect(30+x*55,30+y*55,50,50)
