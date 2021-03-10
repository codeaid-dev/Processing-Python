tiles = [None,None,None,
            None,None,None,
            None,None,None]
xList = [None,None,None,
            None,None,None,
            None,None,None]
yList = [None,None,None,
            None,None,None,
            None,None,None]
first = "O"
second = "X"
turn = False #True:first, False:second
status = 0 #ゲームの手数と終了フラグ1~10、9:全ターン終了、10:ゲーム終了
result = None

def setup():
    global xList, yList
    size(600, 600)
    background(255)
    for i in range(9):
        xList[i] = 100+200*(i%3)
        yList[i] = 130+200*(i/3)

def draw():
    global tiles, xList, yList, first, second, turn, status, result
    #background(255)
    fill(0)
    textSize(100)
    textAlign(CENTER)

    line(200, 0, 200, 600)
    line(400, 0, 400, 600)
    line(0, 200, 600, 200)
    line(0, 400, 600, 400)

    if not result == None:
        return

    if mousePressed:
        id = getID()
        print(id)
        if tiles[id] == None:
            if turn:
                tiles[id] = second
                turn = False
            else:
                tiles[id] = first
                turn = True
            text(tiles[id], xList[id], yList[id])
        result = judge()
        #print(result)
        if result == None:
            return
        else:
            fill(255, 0, 0)
            text(result, 300, 300)

def judge():
    # 同じ柄が並んでいるか確認
    global tiles, status, turn
    if (not tiles[0] == None and tiles[0] == tiles[1] and tiles[0] == tiles[2]) \
    or (not tiles[3] == None and tiles[3] == tiles[4] and tiles[3] == tiles[5]) \
    or (not tiles[6] == None and tiles[6] == tiles[7] and tiles[6] == tiles[8]) \
    or (not tiles[0] == None and tiles[0] == tiles[3] and tiles[0] == tiles[6]) \
    or (not tiles[1] == None and tiles[1] == tiles[4] and tiles[1] == tiles[7]) \
    or (not tiles[2] == None and tiles[2] == tiles[5] and tiles[2] == tiles[8]) \
    or (not tiles[0] == None and tiles[0] == tiles[4] and tiles[0] == tiles[8]) \
    or (not tiles[2] == None and tiles[2] == tiles[4] and tiles[2] == tiles[6]):
        status = 10
        if turn:
            return "O win"
        else:
            return "X win"
    elif status == 9:
        return "Draw"
    return None

def getID():
    # 左上0番目～右下8番目
    if mouseX > 0 and mouseX < 200 and mouseY > 0 and mouseY < 200: #0番目
        return 0
    if mouseX > 200 and mouseX < 400 and mouseY > 0 and mouseY < 200: #1番目
        return 1
    if mouseX > 400 and mouseX < 600 and mouseY > 0 and mouseY < 200: #2番目
        return 2
    if mouseX > 0 and mouseX < 200 and mouseY > 200 and mouseY < 400: #3番目
        return 3
    if mouseX > 200 and mouseX < 400 and mouseY > 200 and mouseY < 400: #4番目
        return 4
    if mouseX > 400 and mouseX < 600 and mouseY > 200 and mouseY < 400: #5番目
        return 5
    if mouseX > 0 and mouseX < 200 and mouseY > 400 and mouseY < 600: #6番目
        return 6
    if mouseX > 200 and mouseX < 400 and mouseY > 400 and mouseY < 600: #7番目
        return 7
    if mouseX > 400 and mouseX < 600 and mouseY > 400 and mouseY < 600: #8番目
        return 8
