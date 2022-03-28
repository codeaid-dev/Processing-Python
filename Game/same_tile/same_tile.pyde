left_x = []    #左側の四角形x座標
left_y = []    #左側の四角形y座標
left_stat = [] #左側の四角形の色（0:白、1:赤）
right_x = []   #右側の四角形x座標
right_y = []   #右側の四角形y座標
right_stat = []#右側の四角形の色（0:白、1:赤）
complete = False
timer = 0

def setup():
    size(500,200)
    for i in range(25):
        left_x.append(50+i%5*30)
        left_y.append(25+i/5*30)
        left_stat.append(int(random(0,2)))
        right_x.append(300+i%5*30)
        right_y.append(25+i/5*30)
        right_stat.append(int(random(0,2)))

def draw():
    global timer
    background(200)
    for i in range(25):
        if left_stat[i] == 0:
            fill(255)
        else:
            fill(255,0,0)
        rect(left_x[i],left_y[i],30,30)
        if right_stat[i] == 0:
            fill(255)
        else:
            fill(255,0,0)
        rect(right_x[i],right_y[i],30,30)

    if complete:
        textSize(50)
        textAlign(CENTER)
        fill(0)
        text("COMPLETE!!",width/2,height/2)
        text(timer,width/2,height/2+60)
        return

    if frameCount % 30 == 0:
        timer += 0.5

    check()

def mousePressed():
    x = mouseX
    y = mouseY
    if complete == False:
        for i in range(25):
            if x>right_x[i] and x<right_x[i]+30 \
            and y>right_y[i] and y<right_y[i]+30:
                if right_stat[i]==0:
                    right_stat[i] = 1
                else:
                    right_stat[i] = 0

def check():
    global complete
    same = 0
    for i in range(25):
        if left_stat[i] == right_stat[i]:
            same += 1
    if same == 25:
        complete = True
