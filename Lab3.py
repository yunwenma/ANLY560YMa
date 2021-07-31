# Created by Yunwen Ma on 2021/7/31
# ANLY 560 Lab3
# The purpose of this program is to draw a shape chosen by the user

import turtle
import time
from turtle import *

print ("This program draws shapes based on the number you enter in a uniform pattern.")
usr_input= input("Enter the the shape you want to draw: square, star, polygon, or type <coolest> for some surprise: ")

#setup window
turtle.setup(400,400)
wn = turtle.Screen()
wn.title("Happy Painting by Yunwen")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

tess.color("green")
tess.pensize(2)

def star():
    for i in range(5):
        tess.forward(50)
        tess.right(144)
    
    turtle.done()

def square():
    for i in range(4):
        tess.forward(50)
        tess.right(90)
    
    turtle.done()

def polygon():
    num_sides = 6
    side_length = 60
    angle = 360/ num_sides
    
    for i in range(num_sides):
        tess.forward(side_length)
        tess.right(angle)
        
    turtle.done()

def coolest():
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    pen = turtle.Pen()
    for x in range(360):
        pen.pencolor(colors[x%6])
        pen.width(x/100 + 1)
        pen.forward(x)
        pen.left(59)
    
    turtle.done()


if usr_input.lower() == 'square':
    square()
elif usr_input.lower() == 'star':
    star()
elif usr_input.lower() == 'polygon':
    polygon()
elif usr_input.lower() == 'coolest':
    coolest()
else:
    print("Please sponsor Yunwen some coffee for further development...")
    

wn.mainloop()
turtle.exitonclick()
