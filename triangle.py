import random
import turtle

k=turtle.Turtle()
n=turtle.numinput("Size","Enter the size of the side:",default=100,minval=50)
colors=turtle.textinput("Color","Enter the color of the triangle")
k.color(colors)
for i in range(3):
    k.forward(n)
    k.right(120)
turtle.exitonclick()

