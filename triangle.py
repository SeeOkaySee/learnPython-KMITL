import turtle
import math 

# set points
x1,y1 = eval(input("point 1: "))
x2,y2 = eval(input("point 2: "))
x3,y3 = eval(input("point 3: "))

# area calculation

# triangle's side length
l1 = math.sqrt((x1-x2)**2 + (y1-y2)**2)
l2 = math.sqrt((x2-x3)**2 + (y2-y3)**2)
l3 = math.sqrt((x1-x3)**2 + (y1-y3)**2)

# heron's formula
s = (l1 + l2 + l3)/2
area =  math.sqrt(s*(s-l1)*(s-l2)*(s-l3))

# initiate turtle
window = turtle.Screen()
window.bgcolor("white")
t = turtle.Turtle()
t.speed(3)
t.width(3)

# start drawing
t.goto(x1,y1)
t.pendown()
t.goto(x2,y2)
t.goto(x3,y3)
t.goto(x1,y1)
t.penup()
t.forward(l1/2)
t.right(90)
t.forward(30)

t.hideturtle()
t.write(area)

turtle.done()
