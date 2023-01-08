from turtle import *
#clcoding.com
from random import randint
def create_rectangle(turtle, color,x, y, width, height):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color) 
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forword(width)
    turtle.left(90)
    turtle.forword(height)
    turtle.left(90)
    turtle.forword(width)
    turtle.left(90)
    turtle.forword(height)
    turtle.left(90)
    turtle.end_fill()
    turtle.setheading(0)
t= Turtle()
y = -100
create_rectangle(t, "red",-15, y-60, 30,60)
width = 240
t.speed(10)
while width > 10:
    width = width - 10
    height = 10
    x = 0 - width - 10
    height = 10
    x = 0 - width/2
    create_rectangle(t, "green",x, y, width,height=)
    y = y + height
    t.speed(1)
    t.penup()
    t.color('blue')
    t.goto(-20, y+10)
t.begin_fill()
t.pandown()
for i in range(5):
    t.forward(40)
    t.right(144)
    t.end_fill()
    tree_height = y + 40
