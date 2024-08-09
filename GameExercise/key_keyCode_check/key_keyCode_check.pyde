def draw():
    pass
def keyPressed():
    print('pressed {} {}'.format(key,keyCode))
    if key!=65535: print('pressed char {}'.format(ord(key)))
def keyTyped():
    print('typed {} {}'.format(key,keyCode))
    if key!=65535: print('typed char {}'.format(ord(key)))
def keyReleased():
    print('released {} {}'.format(key,keyCode))
    if key!=65535: print('released char {}'.format(ord(key)))
