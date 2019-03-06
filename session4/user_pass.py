un = input("username: ")
count = 0
while True:
    if(un == "c4e"):
        pw = input("password: ")
        if(pw == "codethechange"):
            print("Welcome!")
            break
        else:
            print("Sai password")
            count += 1
            if(count == 3):
                break
    else:
        print("Không tìm thấy username!")
        un = input("username: ")

