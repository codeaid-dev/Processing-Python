def setup():
    size(500, 200)
    textSize(50)
    
def draw():
    background(0)
    textAlign(LEFT)
    text("key=", 50, 100)
    text("keyCode=", 50, 150)
    textAlign(RIGHT)
    text(key, 400, 100)
    text(keyCode, 400, 150)
