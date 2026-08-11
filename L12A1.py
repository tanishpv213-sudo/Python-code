import turtle
turtle.Screen().bgcolor("green")
turtle.Screen().setup(600, 700)
polygon = turtle.Turtle()
num_sides = 10
length = 70
angle = 360 / num_sides
for _ in range(num_sides):
    polygon.forward(length)
    polygon.right(angle)

turtle.done()
