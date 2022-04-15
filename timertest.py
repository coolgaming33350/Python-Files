import time
import turtle
start = time.process_time_ns()
turtle.pensize(50)
turtle.circle(100)
print(time.process_time_ns() - start)
