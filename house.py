import turtle

# Create a Turtle object
window = turtle.Screen()
window.bgcolor("white")

t = turtle.Turtle()
t.speed(4)  

# Draw the base of the house
t.penup()
t.goto(-100, -100)
t.pendown()
t.begin_fill()
t.color("yellow")
for _ in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()

# Draw the roof of the house
t.penup()
t.goto(-100, 100)
t.pendown()
t.begin_fill()
t.color("orange")
t.goto(0, 200)
t.goto(100, 100)
t.goto(-100, 100)
t.end_fill()

# Draw the door of the house
t.penup()
t.goto(-30, -100)
t.pendown()
t.begin_fill()
t.color("#A52A2A")
t.goto(-30, -20)
t.goto(30, -20)
t.goto(30, -100)
t.goto(-30, -100)
t.end_fill()

# Draw the window of the house
t.penup()
t.goto(50, 0)
t.pendown()
t.begin_fill()
t.color("light blue")
for _ in range(4):
    t.forward(40)
    t.left(90)
t.end_fill()

#other side
t.penup()
t.goto(-80, 0)
t.pendown()
t.begin_fill()
t.color("light blue")
for _ in range(4):
    t.forward(40)
    t.left(90)
t.end_fill()

#top of the roof
t.penup()
t.goto(0,200)
t.pendown()
t.begin_fill()
t.color("#FF7F50")
t.goto(200,200)
t.goto(300,100)
t.goto(100,100)
t.end_fill()

#house depth
t.begin_fill()
t.color("#FFD700")
t.goto(100,-100)
t.goto(290,-100)
t.goto(290,100)
t.end_fill()

t.hideturtle()

# Exit on click
turtle.done()
