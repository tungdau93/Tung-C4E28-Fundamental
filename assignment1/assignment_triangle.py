from turtle import *

shape('turtle')
speed(0)

forward(100)
color("black","yellow")
begin_fill()
for i in range(2):
    left(120)
    forward(100)
end_fill()
mainloop()