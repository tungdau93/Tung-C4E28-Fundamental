from turtle import *

size = 3
for c in ['red', 'blue', 'brown', 'yellow', 'grey']:
    color(c)
    # size = 3
    for i in range(size):
        forward(100)
        left(360/size)
    size += 1

mainloop()