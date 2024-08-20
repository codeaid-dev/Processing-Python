matrix = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789#$%^&*()*&^%"
font_size = 10
columns = 0
drops = None
def setup():
    global columns,drops
    size(800,600)
    columns = width/font_size
    drops = [0 for _ in range(columns)]

def draw():
    fill(0,10)
    rect(0,0,width,height)
    textSize(font_size)
    for i in range(len(drops)):
        txt = matrix[int(random(len(matrix)))]
        fill(0,255,0)
        text(txt,i*font_size,drops[i]*font_size)
        if drops[i]*font_size > height and random(1)>0.97:
            drops[i] = 0
        drops[i] += 1
