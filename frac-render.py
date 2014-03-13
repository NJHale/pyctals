from turtle import *
from math import *
import turtle





def escDepth (px, py):
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
        row.append(escDepth(x, y))
        x = x + 1
    return row
        

    
def rendBrot ():
    x_0 = -window_width() / 2
    y_0 = window_height() / 2
    x = x_0
    y = y_0
    turtle.tracer(0)
    while y > -y_0:
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
            offset = int(255 * (1 - log(pallet[i][0] / 1000.0 * 255 + 1) / log(256)))
            r = 255 - offset
            if r > 255:
                r = 230
                g = 230
                b = 230
            else:
                g = 0
                b = 255 - offset
                
            turtle.color(r, g, b)
            turtle.down()
            turtle.fd(pallet[i][1])
            turtle.up()
                

        y = y - 1
        turtle.setpos(x, y)
        turtle.update()
    print(y_0)
    print('done')   

           
turtle.speed(0)
turtle.tracer(0)
turtle.up()
turtle.setpos(-window_width() / 2, window_height() / 2)
turtle.down()
colormode(255)
rendBrot()

