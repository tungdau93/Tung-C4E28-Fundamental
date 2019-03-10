def is_inside(a = [], b = []):
    check = True
    x = b[0] + b[2]
    y = b[1] - b[3]
    if((b[0] <= a[0] <= x) and (y <= a[1] <= b[1])):
        return check
    else:
        check = False
        return check

check_inside = is_inside([4, 2], [3, 4, 5, 6])

if(check_inside == True):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
