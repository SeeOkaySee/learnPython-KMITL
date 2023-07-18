import turtle

length = eval(input("input length: "))

#initiate turtle
window = turtle.Screen()
window.bgcolor("white")

t = turtle.Turtle()
t.speed(2)

#start drawing
t.pendown()

for i in [0,1]:
    t.forward(length)
    t.right(144)
    t.forward(length)
    t.right(144)
t.forward(length)
t.right(144)
    

turtle.done()