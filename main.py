from turtle import Turtle, Screen, left, right
import random

# Criação da turtle
tim = Turtle()
tim.shape('turtle')
tim.color('green')

def change_color():
    """Altera a cor da turtle randomicamente"""
    R = random.random()
    B = random.random()
    G = random.random()

    tim.color(R, G, B)

tim.speed(11)
tim.pensize(2)
tim.hideturtle()

# Exercício 1
# lados = 3
# while lados <= 10:
#     for lado in range(lados):
#         tim.forward(100)
#         tim.right(360/lados)
#     lados += 1

# Exercício 2
# for _ in range (0, 40):
#     direction = [0, 90, 180, 270]
#     tim.forward(50)
#     tim.setheading(random.choice(direction))
#     change_color()

x = -450
y = -350
tim.penup()
tim.goto(x, y)

for _ in range (0, 10):
    for _ in range (0, 19):
        tim.dot(10)
        tim.forward(50)
        change_color()
    y += 50
    tim.goto(x, y)

screen = Screen()
screen.exitonclick()
