def is_inside(a = [], b = []):
    check = True
    x = b[0] + b[2]
    y = b[1] - b[3]
    if((b[0] <= a[0] <= x) and (y <= a[1] <= b[1])):
        return check
    else:
        check = False
        return check

point_list = []
rectangle_list = []

for i in range(2):
    p = int(input("Enter your position of point: "))
    point_list.append(p)
print("Position(x, y) of point: ", point_list)
print()
for i in range(2):
    r = int(input("Enter your position of rectangle: "))
    rectangle_list.append(r)
for i in range(2):
    width_height = int(input("Enter your width and height of rectangle: "))
    rectangle_list.append(width_height)
print("Position(x, y), width and height of rectangle: ", rectangle_list)
print()

print(is_inside(point_list, rectangle_list))
