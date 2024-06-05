tiles = []
nums = []
status = [0 for i in range(25)]
count = 1
time = 0
over = False
finish = False
def setup():
    size(500,500)
    textSize(50)
    textAlign(CENTER)
    rectMode(CENTER)

    for i in range(25):
        tiles.append(PVector(50+i%5*100,50+i/5*100))
    while len(nums) != 25:
        n = int(random(1,26))
        if n not in nums:
            nums.append(n)

def draw():
    global time
    background(255)

    if over:
        fill(255,0,0)
        text("GAME OVER",width/2,height/2)
        return
    if finish:
        fill(255,128,0)
        text("FINISH",width/2,height/2)
        text(time,width/2,height/2+50)
        return

    for i in range(25):
        if status[i] == 0:
            fill(255,0,0)
        else:
            fill(255)
        rect(tiles[i].x,tiles[i].y,100,100)
        fill(0)
        text(nums[i],tiles[i].x,tiles[i].y+25)

    time = frameCount / 60.0

def mousePressed():
    global count,over,finish
    x = mouseX
    y = mouseY
    for i in range(25):
        if tiles[i].x-50<x<tiles[i].x+50 \
            and tiles[i].y-50<y<tiles[i].y+50:
            if nums[i] == count:
                status[i] = 1
                if count == 25:
                    finish = True
                count += 1
            else:
                over = True
