import turtle

radius = eval(input("pls input radius:"))
x,y = eval(input("pls input center:"))
area = 3.14 * (radius**2)

turtle.circle(radius)

turtle.penup()
turtle.left(90)
turtle.forward(radius)
turtle.write(area)
turtle.pendown()

turtle.done()