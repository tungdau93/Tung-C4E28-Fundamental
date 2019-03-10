from turtle import *

def draw_star(x, y, length):
    penup()
    goto(x,y)
    pendown()
    color("red")
    for i in range(5):
        right(144)
        forward(length)

draw_star(100, 150, 200)
mainloop()