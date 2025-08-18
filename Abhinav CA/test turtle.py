import turtle

screen = turtle.Screen()
t = turtle.Turtle()

t.fillcolor("red")   # Set the fill color to red
t.begin_fill()       # Start filling

for _ in range(4):
    t.forward(100)
    t.right(90)

t.end_fill()         # End filling, shape gets filled with red

turtle.done()