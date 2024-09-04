import turtle


screen = turtle.Screen()
screen.bgcolor("black") 

t = turtle.Turtle()
t.speed(0)  


colors = [
    "red",
    "blue",
    "yellow",
    "green",
    "orange",
    "purple",
    "white",
    "grey",
    "brown",
    "silver"
]


for x in range(500):
    t.pensize(x / 1000 + 1)
    t.pencolor(colors[x % len(colors)])  
    t.forward(x)
    t.left(59)

# Ocultar la tortuga y finalizar
t.hideturtle()
turtle.done()
