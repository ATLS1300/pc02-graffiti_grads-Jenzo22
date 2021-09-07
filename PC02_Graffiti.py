#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.forward(100)

turtle.goto(100,100)

turtle.goto(0,0)

turtle.up()

turtle.goto(-15, 108)

turtle.dot(30)

turtle.shapesize(2,2,2)

turtle.fillcolor("firebrick4")

turtle.up()

turtle.goto(30,108)

turtle.begin_fill()

turtle.forward(100)

turtle.setheading(180)

turtle.forward(65)

turtle.down()

turtle.forward(40)

turtle.right(90)

turtle.forward(40)

turtle.forward(40)

turtle.right(90)

turtle.forward(40)

turtle.right(90)

turtle.forward(80)

turtle.forward(10)

turtle.forward(5)

turtle.right(90)

turtle.forward(40)

turtle.right(90)

turtle.forward(40)

turtle.fillcolor(51,0,102)

turtle.end_fill()

turtle.up()

turtle.goto(111,-90)

turtle.shapesize(6,6,6)

turtle.setheading(180)

turtle.forward(100)

turtle.down()

turtle.setheading(0)

turtle.forward(100)

turtle.left(90)

turtle.forward(5)

turtle.left(90)

turtle.forward(100)

turtle.left(90)

turtle.forward(5)

turtle.pensize(5)

turtle.shapesize(2,2,2)

turtle.forward(5)

turtle.forward(245)

turtle.goto(0,0)

turtle.setheading(180)

turtle.forward(200)

turtle.bye()
#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
