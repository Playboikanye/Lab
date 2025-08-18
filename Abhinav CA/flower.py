import turtle

def draw_petal(t, radius, angle):
    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)

def draw_flower(petals=5, radius=100, angle=60):
    t = turtle.Turtle()
    t.speed(3)
    t.color("magenta")

    for _ in range(petals):
        draw_petal(t, radius, angle)
        t.left(360 / petals)

    t.hideturtle()
    turtle.done()

user_input = turtle.textinput("Petal Input", "Enter the number of petals:")

if user_input and user_input.isdigit():
    petal_count = int(user_input)
    if petal_count > 0:
        draw_flower(petals=petal_count)
    else:
        print("Please enter a positive number.")
else:
    print("Invalid input or canceled.")
