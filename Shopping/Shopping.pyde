apple=120
peach=180
grape=200

background(0)
size(500,500)
textSize(30)

textAlign(LEFT)
text("Apple: 120 yen", 10, 100)
text("Peach: 180 yen", 10, 150)
text("Grape: 200 yen", 10, 200)
text("--- Total(tax included): --- ", 10, 250)
text((apple+peach+grape)*1.1, 10, 300)
