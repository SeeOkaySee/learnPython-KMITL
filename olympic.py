import turtle

r = eval(input("Radius= "))

# initiate turtle
window = turtle.Screen()
window.bgcolor("white")
turtle.width(20)

# start drawing
turtle.color("blue")
turtle.penup()
turtle.goto(-r, r)
turtle.pendown() 
turtle.circle(r)

turtle.color("black")
turtle.penup()
turtle.goto(r, r)
turtle.pendown() 
turtle.circle(r)

turtle.color("red")
turtle.penup()
turtle.goto(r*3, r)
turtle.pendown()
turtle.circle(r)

turtle.color("yellow")
turtle.penup() 
turtle.goto(0, -r+10)
turtle.pendown ()
turtle.circle(r)

turtle.color("green")
turtle.penup()
turtle.goto(r*2, -r+10)
turtle.pendown() 
turtle.circle(r)

turtle.done()