from turtle import *

for i in ["red", "blue", "brown", "yellow", "grey"]:
    color(i)
    begin_fill()
    forward(50)
    for i in range(2):
        right(90)
        forward(100)
        right(90)
        forward(50)
    end_fill()

mainloop()