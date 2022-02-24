x,y = 0,0
row,col = 0,0
def setup():
    size(450,450)

def draw():
    global x,y,row,col
    if frameCount % 60 == 0:
        x = col%9*50
        y = row%9*50
        if x >= width and y >= height:
            return
        fill(255)
        rect(x,y,50,50)
        col += 1
        if col%9 == 0:
            row += 1
