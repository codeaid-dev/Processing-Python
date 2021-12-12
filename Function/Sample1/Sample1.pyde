def threeCircle(x, y, w):
    ellipse(x, y, w, w)
    ellipse(x+w, y, w, w)
    ellipse(x+w*2, y, w, w)

size(300, 300)
background(0)
fill(255)
threeCircle(100, 150, 50)
