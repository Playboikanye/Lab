import turtle
a=0
k=turtle.Turtle()
num=turtle.numinput("NO.","Enter the no0. of triangles",default=2,minval=1)
a=num 
k.width(10)
k.begin_fill() 
for j in range(int(a)):
    n=turtle.numinput("Size","Enter the size of the side:",default=100,minval=50)
    for i in range(3):
        k.forward(n)
        k.left(120)
    k.penup()
    k.forward(n+20)
    k.pendown()

k.hideturtle()
turtle.exitonclick()