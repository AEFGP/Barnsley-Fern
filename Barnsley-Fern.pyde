

x,y = 0,0
ctr = 0
li = []

def setup():
    global x,y, ctr, li
    size(600, 600)
    background(128)
    frameRate(50)
    stroke(0, 255, 0)
    strokeWeight(1)
    for i in range(100000):
        fern()
    

def fern():
    global x,y, ctr, li
    px = map(x, -2.1820, 2.6558, 0, width)
    py = map(y, 0, 9.998, height, 0)
    
    li.append((px,py))
    x, y = transform(x,y)
    #print(px, py)

def draw():
    for x,y in li:
        point(x,y)
    

def transform(x, y):
    r = random(1)
    #print(r)
    #nextX, nextY = 0, 0
    if r < 0.01:
        nextX =  0
        nextY = 0.16 *  y 
        
    elif r < 0.86:
        nextX =  0.85 * x + 0.04 * y
        nextY = -0.04 * x + 0.85 * y + 1.6
        
    elif r < 0.93:
        nextX =  0.20 * x - 0.26 * y
        nextY =  0.23 * x + 0.22 * y + 1.6
        
    else:
        nextX = -0.15 * x + 0.28 * y
        nextY =  0.26 * x + 0.24 * y + 0.44
        
    
    return (nextX, nextY)
    
