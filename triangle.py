def triangle(int n):
    import turtle
    k=turtle.Turtle()
    for i in range(3):
    k.forward(n)
    k.right(120)

n=int(input("Enter the length: "))
triangle(n)


    