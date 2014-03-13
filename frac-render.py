from turtle import *
import turtle 

def palMax (pallet):
    pmax = 0;
    for i in range(0, len(pallet)):
        cur = pallet[i][0]
        if pmax < cur :
            pmax = cur
    return pmax

def localPalMax (pallet, i, a):
    lpmax = 0;
    j = 0
    while i + j < len(pallet) and i - j >= 0 and j < a:
        ahead  = pallet[i + j][0]
        behind = pallet[i - j][0]
        if ahead > lpmax:
            lpmax = ahead
        if behind > lpmax:
            lpmax = behind
        j = j + 1
    return lpmax



def brotDepth (px, py):
    maxDepth = 5000;
    x = 0
    y = 0
    xScaled = (1 - (-2.5)) *(px - ( - window_width() / 2)) / (window_width() / 2 - (- window_width() / 2)) + -2.5 #x coordinate normalized to mandelbrot domain
    yScaled = (1 - (-1)) *(py - ( - window_height() / 2)) / (window_height() / 2 - (- window_height() / 2)) + -1#y coordinate normalized to mandelbrot range

    depth = 0
    while depth < maxDepth and (x * x + y * y) < 4:
        xTemp   = x * x - y * y + xScaled
        y       = 2 * x * y + yScaled
        x       = xTemp
        depth   = depth + 1

    return depth

def depthRow (x, y):
    row = []
    for i in range(0, window_width()):
        row.append(brotDepth(x, y))
        x = x + 1
    return row
        

    
def rendBrot ():
    a = -window_width() / 2
    b = window_height() / 2
    x = a
    y = b
    turtle.tracer(0)
    print(b)
    while y > -b:
        row    = depthRow(x, y)
        pallet = [] 
        i = 0
        while i < len(row):
            j = i
            while j < len(row) and row[j] == row[i]:
                j = j + 1
            pallet.append([row[i], j - i])
            if j > i :
                i = j
            else:
                i = i + 1
        
        for i in range(0, len(pallet)):
            lmax = localPalMax(pallet, i, 2)
            r = 0
            g = 0
            b = 0
            if (255) * (pallet[i][0]) / lmax != 255:
                b = (255) * (pallet[i][0]) / (lmax)
                r = 255 - b
                g = 0
                
            turtle.color(r, g, b)
            turtle.down()
            turtle.fd(pallet[i][1])
            turtle.up()
                

        y = y - 1
        turtle.setpos(x, y)
        turtle.update()
    print('done')   

           
turtle.speed(0)
turtle.tracer(0)
turtle.up()
turtle.setpos(-window_width() / 2, window_height() / 2)
turtle.down()
colormode(255)
rendBrot()

