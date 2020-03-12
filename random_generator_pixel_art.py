# Original code: Pixel Art - http://www.101computing.net/pixel-art-in-python/
import turtle
from random import randint, choice # I add the ramdomness

myPen = turtle.Turtle()
#myPen.tracer(0)
myPen.speed(0)
myPen.color("#000000")
# add the  dictionary
colourPalette = {'a': "#FF0000",
                 'b': "#00FF00",
                 'c': "#0000FF",
                 'd': "#000000",
                 'e': "#FFFFFF"}


# This function draws a box by drawing each side of the square and using the fill function
def box(intDim):
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 270 deg.
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)


boxSize = 10
# Position myPen in top left area of the screen
myPen.penup()
myPen.forward(-100)
myPen.setheading(90)
myPen.forward(100)
myPen.setheading(0)


# Here is how your PixelArt is stored (using a "list of lists")
# Generate on the fly the box, the rows, fill the rows and fill the box
row = []
pixels = []
for r in range(16):
    row.append(randint(0, 1))
    for b in range(1):
        pixels.append(row)

L = ['a', 'b', 'c', 'd', 'e']  # call to key dict
for i in range(0, len(pixels)):
    for j in range(0, len(pixels[i])):
        if pixels[i][j] == 1:
            box(boxSize)
        myPen.penup()
        myPen.color(colourPalette[choice(L)])  # add color randomly by choice
        myPen.forward(boxSize)
        myPen.pendown()
    myPen.setheading(270)
    myPen.penup()
    myPen.forward(boxSize)
    myPen.setheading(180)
    myPen.forward(boxSize * len(pixels[i]))
    myPen.setheading(0)
    myPen.pendown()

myPen.getscreen().update()
