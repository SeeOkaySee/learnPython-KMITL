import turtle

# user inputs coordinates
x0,y0 = eval(input("Coordinates of P0 (x,y): "))
x1,y1 = eval(input("Coordinates of P1 (x,y): "))
x2,y2 = eval(input("Coordinates of P2 (x,y): "))

# p2 calculating method
if abs(x2-x1) > abs(x2-x0):
    print("p2 is on the left side of the line between p0 & p1")
elif abs(x2-x0) > abs(x2-x1):
    print("p2 is on the right side of the line between p0 & p1")
else:
    print("p2 is exactly at the middle of the line")

#start drawing
t = turtle.Turtle()

t.penup()
t.goto(x0,y0)
t.pendown()
t.goto(x1,y1)
t.penup()
t.goto(x0,y0)
t.right(90)
t.forward(5)
t.write("P0")
t.goto(x1,y1)
t.right(90)
t.forward(5)
t.write("P1")
t.goto(x2,y2)
t.right(90)
t.forward(5)
t.write("P2")

turtle.done()