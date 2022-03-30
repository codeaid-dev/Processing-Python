tiles = []
nums = []

def setup():
    size(450,450)
    textSize(75)
    textAlign(CENTER)
    rectMode(CENTER)
    for i in range(9):
        tiles.append(PVector(75+i%3*150,75+i/3*150))

    while len(nums) < 9:
        n = int(random(9))
        if n not in nums:
            nums.append(n)

def draw():
    for i in range(9):
        fill(255)
        rect(tiles[i].x,tiles[i].y,150,150)
        if nums[i] != 0:
            fill(0)
            text(nums[i],tiles[i].x,tiles[i].y+35)

def mousePressed():
    x = mouseX
    y = mouseY
    for i in range(9):
        if tiles[i].x-75<x<tiles[i].x+75 \
        and tiles[i].y-75<y<tiles[i].y+75:
            slide(i)

def slide(i):
    if i<=5 and nums[i+3] == 0:
        nums[i], nums[i+3] = nums[i+3], nums[i]
    if i>=3 and nums[i-3] == 0:
        nums[i], nums[i-3] = nums[i-3], nums[i]
    if i%3 != 2 and nums[i+1] == 0:
        nums[i], nums[i+1] = nums[i+1], nums[i]
    if i%3 != 0 and nums[i-1] == 0:
        nums[i], nums[i-1] = nums[i-1], nums[i]
