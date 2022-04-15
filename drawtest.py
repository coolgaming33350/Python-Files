import turtle
yeslist = ("yes", "y", "YES", "Yes", "yas", "Yas", "ye", "Ye")

t = turtle.Turtle("turtle")

colour = input("What color would you like to use?\n(DONT USE A HASH before the code if you use hex!):")

ishexcode = int(len(colour))
if ishexcode >= 6:
    guarentee = input("Is this a hex code? (yes or no): ")
    if guarentee in yeslist:
        t.color("#" + colour)
        print("Use alt+tab to see the window!")
    else:
        t.color(colour)
        print("Use alt+tab to see the window!")
        

from turtle import Screen
screen = Screen()
t.speed(-1)
t.pensize(10)

def dragging(x, y):
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)

def clickRight(clickRight, x):
    t.clear()

def main():
    turtle.listen()
    
    t.ondrag(dragging)  
    turtle.onscreenclick(clickRight, 3)

    screen.mainloop()  

main()


