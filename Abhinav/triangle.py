import turtle
k=turtle.Turtle()
screen=turtle.Screen()
n=turtle.numinput("Size","Enter the size of the side:",default=100,minval=50)
bgcol=turtle.textinput("BGColor","Enter the color of the background")
screen.bgcolor(bgcol)
colors=turtle.textinput("Color","Enter the color of the triangle")
k.fillcolor(colors)  
k.begin_fill()  
for i in range(3):

    k.forward(n)
    k.right(120)
k.end_fill()

k.hideturtle()
turtle.exitonclick()