import turtle

ninja = turtle.Turtle()

ninja.speed(10)


for i in range(360):
    ninja.color("blue")
    ninja.forward(100)
    ninja.right(15)
    ninja.color("red")
    ninja.forward(50)
    ninja.color("red")
    ninja.right(15)
    ninja.color("blue")
    ninja.forward(20)
    ninja.left(60)
    ninja.color("green")
    ninja.forward(50)
    ninja.right(30)

    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(1)

turtle.done()
