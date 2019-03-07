car = {}
inp = input("Your words: ").lower()
list_inp = list(inp)
list_inp.sort()
# print(list_inp)
print(list_inp)
for i in list_inp:
    car[i] = car.get(i, 0) + 1
# print(car)
for i, j in car.items():
    if(i != " "):
        print(i, j)


