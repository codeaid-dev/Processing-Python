class Snow:
    def __init__(self):
        self.x = random(width)
        self.y = random(-height,height)
        self.z = random(0.2,1.0) # 1に近いほど手前

        self.speed = map(self.z,0.2,1.0,0.5,4.0) # 手前ほど速い
        self.radius = map(self.z,0.2,1.0,0.75,3.5) # 手前ほど大きい

        self.angle = random(TWO_PI)
        self.swing1 = random(0.01,0.03)
        self.swing2 = map(self.z,0.2,1.0,0.2,1.5) # 手前ほど横揺れが大きい

    def update(self):
        self.y += self.speed
        self.angle += self.swing1
        self.x += sin(self.angle)*self.swing2
        if self.y > height:
            self.y = random(-50,0)
            self.x = random(width)
        if self.x < 0:
            self.x = width
        elif self.x > width:
            self.x = 0
        # 雪が地面に到着
        ix = constrain(int(self.x),0,width-1)
        if self.y+self.radius >= ground[ix]:
            fallenSnow(ix,self.radius*2*0.3) # 積雪
            self.reset() # 新しい雪を上から降らせる

    def draw(self):
        noStroke()
        fill(255)
        circle(self.x,
               self.y,
               self.radius*2)

    def reset(self):
        self.x = random(width)
        self.y = random(-100,-10)
        self.z = random(0.2,1.0)
        self.speed = map(self.z,0.2,1.0,0.5,4.0)
        self.radius = map(self.z,0.2,1.0,0.75,3.5)
        self.swing2 = map(self.z,0.2,1.0,0.2,1.5)

snows = []
ground = None

def setup():
    global ground
    size(600,600)
    ground = [height]*width
    for i in range(200):
        snows.append(Snow())

def draw():
    background(0)
    for snow in snows:
        snow.update()
        snow.draw()
    # 雪の面積を少しずつ平らにする
    smoothSnow()
    drawGround()

# 雪を積もらせる
def fallenSnow(x, amount):
    # 周辺に少し広げる
    for i in range(-3,4):
        ix = x + i
        if ix >= 0 and ix < width:
            # 中央ほど多く積もる
            weight = 1.0 - abs(i) / 4.0
            ground[ix] -= amount * weight
    # 雪が画面上まで来ないようにする
    for i in range(width):
        ground[i] = max(ground[i], 250)

# 積もった雪を描画
def drawGround():
    noStroke()
    fill(255)
    beginShape()
    # 左上から
    vertex(0,ground[0])
    # 地面の雪のライン
    for x in range(width):
        vertex(x,ground[x])
    # 画面下
    vertex(width,height)
    vertex(0,height)
    endShape(CLOSE)

def smoothSnow():
    newGround = [0]*width
    # 周囲の雪を均す
    for i in range(width):
        if i==0 or i==width-1:
            newGround[i] = ground[i]
        else:
            newGround[i] = \
            (ground[i-1] + ground[i] + ground[i+1]) / 3.0
    # 少しずつ平均値に近づける
    for x in range(width):
        ground[x] = \
        lerp(ground[x], newGround[x], 0.05)
