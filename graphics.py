import time
import random
import turtle

screen = turtle.Screen()
screen.setup(700, 600)
screen.title('Test Graphics!')

tim = turtle.Turtle()

tim.color('#00ff64', '#00ffff')
tim.pensize(10)
tim.shape('arrow')
tim.speed(-1)
tim.goto(0,200)

for x in range(4):
    tim.begin_fill()
    tim.forward(100)
    tim.left(90)
    tim.end_fill()

for x in range(3):
    tim.begin_fill()
    tim.pensize(5)
    tim.circle(50)
    tim.forward(50)
    tim.end_fill()

tim.forward(100)
tim.goto(-200, 100)
for x in range(5):
    tim.color('red', 'blue')
    tim.forward(100)
    tim.begin_fill()
    tim.circle(50)
    tim.end_fill()
tim.hideturtle()
tim.right(90)
tim.forward(100)
tim.left(90)
tim.showturtle()

for x in range(5):
    tim.begin_fill()
    tim.forward(100)
    tim.right(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(150)
