# usr/bin/env/python3
# Call modules
import turtle
from random import randint
import random

# variables
running = True
# Define standard angles
right = 90
acute = 45
half_obtuse = 120
obtuse = 135
flat = 180
# define the metric
meter = 100
# define the window
turtle.setup(600, 600)
turtle.bgcolor("lightgrey")
turtle.title('Algorithmic random Human Art Generator')
turtle.pensize(3)

# Functions
def color():
    """Give random color"""
     R = random.random()
     G = random.random()
     B = random.random()
     turtle.color(R, G, B)

# Draw figures

def square():
    """Draw square"""
    turtle.pendown()
    for side in range(4):
        turtle.forward(meter)
        turtle.left(right)
    turtle.penup()

def rectangle():
    """Draw rectangle"""
    turtle.pendown()
    for side in range(2):
        turtle.forward(2 * meter)
        turtle.left(right)
        turtle.forward(meter)
        turtle.left(right)
    turtle.penup()

def triangle():
    """Draw triangle"""
    turtle.pendown()
    for sido in range(3):
        turtle.forward(meter)
        turtle.left(half_obtuse)
    turtle.penup()

def circle():
    """Draw a circle"""
    turtle.pendown()
    turtle.circle(50)
    turtle.penup()

def spinning_squares():
    """Generate three spinning scares by a turtle"""
    turtle.pendown()
    turtle.left(flat)
    turtle.up()
    turtle.forward(3*meter)
    turtle.down()
    iteration = 1
    while iteration <= 3:
        turtle.right(obtuse)
        square()
        iteration += 1
    turtle.penup()

def spiral():
    """Draw spiral"""
    turtle.pendown()
    for i in range(1, 50):
        turtle.forward(meter)
        turtle.left(92)
        side = meter + 7
    turtle.penup()

while running:
    """Main loop"""
    message = """Enter triangle, square, rectangle, circle, 
                 spinning squares, spiral or exit: """
    entered = input(message)
    x = randint(0, 300)
    y = randint(0, 300)
    turtle.begin_fill()
    color()
    turtle.goto(x, y)
    if entered == 'triangle':
        triangle()
        turtle.end_fill()
    elif entered == 'square':
        square()
        turtle.end_fill()
    elif entered == 'rectangle':
        rectangle()
        turtle.end_fill()
    elif entered == 'circle':
        circle()
        turtle.end_fill()
    elif entered == 'spinning squares':
        spinning_squares()
        turtle.end_fill()
    elif entered == 'spiral':
        spiral()
    elif entered == 'exit':
        running == 'false'
        print('Exiting...Oh! I forget, click in window for close. :-)')
        break;
    else:
        print('Not a command.')

print('Bye!')

turtle.exitonclick()