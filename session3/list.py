#List/ Array
# menu = ["Cơm", "Bún", "Phở", "Bún"]
# menu.append("Bánh cuốn") #Thêm phần thử vào sau cùng của list
# print(*menu, sep=", ") #sep: thêm dấu phẩy ở sau mỗi các phần tử trong list
# menu.remove("Bún") #remove: xóa giá trị xuất hiện đầu tiên chứ ko phải tất cả
# print(*menu, sep=", ")


#exercies: thêm 1 phần thử từ người dùng vào list ban đầu
# fav = ["death note", "netflix", "teaching"]
# print("Hi there, here you favorite things so far:")
# print(*fav, sep=", ")
# print("Name one thing you want to add?", end=" ")
# name = input("")
# fav.append(name)
# print(*fav, sep=", ")

# 3 loop with: cách đọc list
# loop with item: Hiện ra các phần tử của list
# menu = ["Cơm", "Bún", "Phở", "Thịt", "Rau"]
# for item in menu:
#     print(item)


# loop with index: hiện ra các vị trí của từng phần tử trong list
# menu = ["Cơm", "Bún", "Phở", "Thịt", "Rau"]
# for index in range(len(menu)):
#     print(index)

# loop with item,index: Hiện ra tất cả vị trí, tên của từng phần tử trong list
# menu = ["Cơm", "Bún", "Phở", "Thịt", "Rau"]
# for index, item in enumerate(menu):
#     print(index+1, item)


# update: sửa xóa list
# menu = ["Cơm", "Bún", "Phở", "Thịt", "Rau"]
# menu[0] = "Cháo" # sửa vị trí đầu tiên của list
# print(menu)


#ex: sửa một vị trí bất kì trong list
# fav = ["death note", "netflix", "teaching"]
# print("Hi there, here you favorite things so far:")
# print("******************************************")
# for index, item in enumerate(fav):
#     print(index+1, item, sep=" ")
# print("******************************************")
# n = int(input("Position you want to update?"))
# m = input("Your replacing favorite?")
# fav[n-1] = m
# for index, item in enumerate(fav):
#     print(index+1, item, sep=" ")



# delete trong list
# menu = ["Cơm", "Bún", "Phở", "Thịt", "Rau"]
# # menu.pop(1) # Xóa phần tử ở vị trí số 1 trong list
# del menu[2] # Xóa phần tử ở vị trí số 2 trong list
# print(*menu, sep=", ")


#ex: xóa một vị trí bất kì trong list
# fav = ["death note", "netflix", "teaching"]
# for index, item in enumerate(fav):
#     print(index+1, item, sep = ". ")
# n = int(input("Favorite position you want to delete?"))
# del fav[n-1] # xóa giá trị của vị trí [n-1] trong list
# # fav.pop(n-1)    # xóa giá trị của vị trí [n-1] trong list. Nếu ko xác định được vị trí, xóa gtrị của vtrí cuối cùng
# # fav.remove("hello")
# for index, item in enumerate(fav):
#     print(index+1, item, sep = ". ")



menu = ["Cơm", "Bún", "Phở", "Bún"]
x = menu.count("Phở")
print(x)
