# vòng while chỉ chạy khi biểu thức đúng

# count = 0
# while (count<3):
#     count += 1
#     print("Hello")

# count = 0
# loop = True
# while loop:
#     print("Hello")
#     count += 1
#     if(count == 3):
#         # loop = False #(điều kiện của biểu thức. Vẫn thực hiện các câu lệnh dưới nó)
#         break #(break là thoát luôn ra khỏi vòng lặp. ko thực hiện các câu lệnh dưới nó)
#         print("Hello") #dòng này để check xem sự khác nhau giữa break với true false


# nhập vào số tự nhiên. So sánh số vừa nhập vừa số trong random. Chỉ được đoán 7 lần
# from random import *
# c = randint(0,100)
# print(c)
# count = 0
# loop = True
# while loop:
#     if(count < 7):
#         a = int(input("Nhập số tự nhiên bất kỳ(0-100): "))
#         if(a < c):
#             print("Số bạn nhập nhỏ hơn số random")
#         elif(a > c):
#             print("Số bạn nhập lớn hơn số random")
#         else:
#             print("Số bạn nhập bằng số random.Win")
#             loop = False
#         count += 1
#     else:
#         print("Thua cmnr")
#         loop = False
# chỉnh lại

# Nhập vào 1 số tự nhiên. Đếm các chữ số của số đó.
# n = int(input("Nhập số tự nhiên bất kỳ: "))
# count = 0
# while(n > 0):
#     n = n//10
#     count += 1
# print(count)
