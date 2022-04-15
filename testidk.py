import turtle

size = int(('1'))

tim = turtle.Turtle()

tim.color('#00ff64')
tim.pensize(size)
tim.shape('arrow')
tim.speed(-1)
tim.goto(0,200)

for x in range(100000):
    tim.goto(0,0)
    size = int((size + 10))
    tim.pensize(size)
pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
