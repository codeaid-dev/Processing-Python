class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mine = False
        self.open = False
        self.flag = False
        self.count = 0

SIZE = 10
MINE_COUNT = 15
cells = []
bomb,hata = None,None
gameOver = False
openCount = 0

def setup():
    global bomb,hata
    size(500,500)
    bomb = loadImage("bakudan50x50.png")
    hata = loadImage("flag_red40x50.png")
    # create board
    for y in range(SIZE):
        for x in range(SIZE):
            cells.append(Cell(x, y))
    # set bomb
    mineCount = 0
    while mineCount<MINE_COUNT:
        index = int(random(len(cells)))
        cell = cells[index]
        # already bomb, go to next
        if cell.mine: continue
        cell.mine = True
        mineCount += 1
    # check the neighbor bomb
    for cell in cells:
        fill(128)
        rect(cell.x*50,cell.y*50,50,50)
        if cell.mine: continue
        count = 0;
        for dy in range(-1,2):
            for dx in range(-1,2):
                if dx == 0 and dy == 0:
                    continue
                x = cell.x+dx
                y = cell.y+dy
                if x<0 or x>=SIZE or y<0 or y>=SIZE:
                    continue
                neighbor = cells[y*SIZE+x]
                if neighbor.mine:
                    count += 1
        cell.count = count
    stroke("#2f4f4f")

def draw():
    pass

# open cell
def openCell(cell):
    global gameOver,openCount
    if gameOver: return
    if cell.open: return
    if cell.flag: return
    cell.open = True
    openCount += 1
    # It's bomb
    if cell.mine:
        fill(255,0,0)
        rect(cell.x*50,cell.y*50,50,50)
        image(bomb,cell.x*50,cell.y*50)
        gameOver = True
        showAllMines()
        textAlign(CENTER,CENTER)
        textSize(50)
        fill(255,0,255)
        text("Game Over", width/2, height/2)
        return
    # show black rect
    fill(0)
    rect(cell.x*50,cell.y*50,50,50)
    # show neighbor bombs
    if cell.count > 0:
        textAlign(CENTER,CENTER)
        textSize(40)
        fill(255)
        text(cell.count,cell.x*50+25,cell.y*50+25)
    else:
        # If no neighbor bombs, open cell auto
        openNeighbors(cell)
    # check clear
    checkClear()

# open neighbor cell
def openNeighbors(cell):
    for dy in range(-1,2):
        for dx in range(-1,2):
            if dx == 0 and dy == 0:
                continue
            x = cell.x+dx
            y = cell.y+dy
            if x<0 or x>=SIZE or y<0 or y>=SIZE:
                continue
            neighbor = cells[y*SIZE+x]
            if not neighbor.mine and \
                not neighbor.open and \
                not neighbor.flag:
                openCell(neighbor)

# show all bombs
def showAllMines():
    for cell in cells:
        if cell.mine:
            fill(255,0,0)
            rect(cell.x*50,cell.y*50,50,50)
            image(bomb,cell.x*50,cell.y*50)

# check clear or not
def checkClear():
    global gameOver
    safeCellCount = SIZE * SIZE - MINE_COUNT
    if openCount == safeCellCount:
        gameOver = True
        fill(255,0,0)
        textAlign(CENTER,CENTER)
        textSize(50)
        fill(0,0,255)
        text("Game Clear", width/2, height/2)

def mousePressed():
  # mouse left press
  if mouseButton == LEFT:
    for cell in cells:
      if cell.x*50 < mouseX and cell.x*50+50 > mouseX \
          and cell.y*50 < mouseY and cell.y*50+50 > mouseY:
        openCell(cell)
