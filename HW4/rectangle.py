import turtle

# user input
x1, y1 = eval(input("Enter center coordinates (x,y) for Rectangle 1: "))
width1, height1 = eval(input("Enter width and height for Rectangle 1: "))

x2, y2 = eval(input("Enter center coordinates (x,y) for Rectangle 2: "))
width2, height2 = eval(input("Enter width and height for Rectangle 2: "))

#function for checking overlaps
def checkrec(rect1, rect2):
    x1, y1, width1, height1 = rect1
    x2, y2, width2, height2 = rect2

    if (x1 - width1 / 2 >= x2 + width2 / 2 or
        x1 + width1 / 2 <= x2 - width2 / 2 or
        y1 - height1 / 2 >= y2 + height2 / 2 or
        y1 + height1 / 2 <= y2 - height2 / 2):
        print("Rectangles do not overlap")
    if (x1 - width1 / 2 >= x2 - width2 / 2 and
        x1 + width1 / 2 <= x2 + width2 / 2 and
        y1 - height1 / 2 >= y2 - height2 / 2 and
        y1 + height1 / 2 <= y2 + height2 / 2):
        print("Rectangle 1 is inside Rectangle 2")
    if (x2 - width2 / 2 >= x1 - width1 / 2 and
        x2 + width2 / 2 <= x1 + width1 / 2 and
        y2 - height2 / 2 >= y1 - height1 / 2 and
        y2 + height2 / 2 <= y1 + height1 / 2):
        print("Rectangle 2 is inside Rectangle 1")
    else:
        print("Rectangles overlap")

# rectangle for loop
def draw_rectangle(x, y, width, height):
    turtle.penup()
    turtle.goto(x - width / 2, y - height / 2)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

# Draw
draw_rectangle(x1, y1, width1, height1)
draw_rectangle(x2, y2, width2, height2)

result = checkrec((x1, y1, width1, height1), (x2, y2, width2, height2))
turtle.penup()
turtle.goto(0, -250)
turtle.pendown()
turtle.write(result)

turtle.done()
