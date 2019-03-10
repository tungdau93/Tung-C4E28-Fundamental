x = int(input("x = "))
y = int(input("y = "))
ip = input("nhap phep tinh: ")
ketqua = 0

if(ip == "+"):
    ketqua = x + y
elif(ip == "-"):
    ketqua = x - y
elif(ip == "*"):
    ketqua = x * y
elif(ip == "/"):
    ketqua = x / y
else:
    print("Invalid")

print(ketqua)

