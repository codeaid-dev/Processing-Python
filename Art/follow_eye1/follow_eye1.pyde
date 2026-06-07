class Eye:
  def __init__(self, x, y, radius):
    self.x = x;
    self.y = y;
    self.radius = radius;
    self.inRadius = radius/2;
    self.iro = color(255);
    self.inIro = color(0);

eyes = [];

def setup():
  size(500,500)
  noStroke()
  for i in range(50):
    radius = random(5,31)
    x = random(radius,width-radius)
    y = random(radius,height-radius)
    eyes.append(Eye(x,y,radius))

def draw():
  background(0)
  for eye in eyes:
    followEye(eye);

def followEye(eye):
  fill(eye.iro)
  ellipse(eye.x,eye.y,eye.radius*2,eye.radius*2)
  angle = atan2(mouseY-eye.y,mouseX-eye.x)
  move = eye.radius-eye.inRadius
  fill(eye.inIro)
  ellipse(eye.x+cos(angle)*move,
          eye.y+sin(angle)*move,
          eye.inRadius*2,eye.inRadius*2)
