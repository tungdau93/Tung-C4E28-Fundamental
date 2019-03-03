from turtle import *
# khởi tạo con rùa
shape ('turtle')
speed(0)

# vòng lặp 500 lần
for i in range(500):
    for j in range(4):
        forward(100)
        left(90)
        
    left(7)

#chọn màu cho hình vẽ
# color("red","yellow")
# begin_fill()
# for j in range(4):
#     forward(100)
#     left(90)
# end_fill()

#vẽ hình vuông nét đứt
# for k in range(4):
#     forward(50)
#     penup()
#     forward(50)
#     pendown()
#     left(90)

# vẽ hình tròn
# circle(100)
mainloop()