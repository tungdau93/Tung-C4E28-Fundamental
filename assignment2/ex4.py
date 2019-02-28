print("a. 20x1 stars:\n")
a = "*"
print(*a*20)


print("=====================================================")
print("b. n start (n is entered by users)")
n = int(input("Enter a number: "))
print("\n",*a*n)


print("=====================================================")
print("c. 9 stars and xs in total\n")
b = "x*"
print(*(b*4), "x")


print("=====================================================")
print("d. m stars and xs in total (m is entered by users)")
m = int(input("Enter a number: "))
print()

for i in range(m):
    if(i%2 == 0):
        print("x", end = " ")
    else:
        print("*", end = " ")
# if(m%2 == 0):
#     c = ["x *" for i in range(int(m/2))]
#     print(*c)
# else:
#     c = ["x *" for i in range(int(m/2))]
#     print(*c,"x")


print("\n=====================================================")
print("f. 7x3 stars\n")
for i in range(3):
    print(*a*7)


print("=====================================================")
print("g. x x y stars (x, y are entered by users)")
x = int(input("Enter x: "))
y = int(input("Enter y: "))
print()
for i in range(y):
    print(*a*x)
