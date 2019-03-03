# yob = int(input("Enter your yob: "))
# age = 2019-yob
# # câu lệnh điều kiện if
# if(age < 10):
#     print("baby")
# elif(age<18):
#     print("teenager")
# else:
#     print("not baby")


# random từ 0 ->100. từ khóa randint được lấy từ thư viện random. lấy ngẫu nhiên 1 số bất kì trong khoảng range
# from random import randint
# x = randint(0,100)
# print(x)


# from random import randint
# Lệnh randint là để lấy ngẫu nhiên 1 số bất kì trong 1 khoảng nào đó(0 đến 100)
# x = randint(0,100)
# print(x)
# if(0<=x<36):
#     print("sunny")
# elif(x<71):
#     print("rainy")
# else:
#     print("cloudy")


# giai phuong trinh bac 2
# from math import sqrt
# print("ax2 + bx + c")
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
# delta = b**2 - 4*a*c
# if(delta > 0):
#     print("Phương trình có 2 nghiệm phân biệt")
#     print("Nghiem thu 1: ", float((-b+sqrt(delta))/(2*a)))
#     print("Nghiem thu 2: ", float((-b-sqrt(delta))/(2*a)))
# elif(delta == 0):
#     print("phương trình có nghiệm kép")
#     print("Nghiệm kép: ", float(-b/(2*a)))
# else:
#     print("Phương trình vô nghiệm")


# Nhập 2 số bất kì. Tìm số chẵn trong khoảng 2 số đã nhập
# n = int(input("n = "))
# m = int(input("m = "))
# print("Các số chẵn nằm trong khoảng", n, "và",m, "là: ")
# for i in range(n,m+1):
#     if(i%2 == 0):
#         print(i)
