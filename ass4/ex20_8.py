car = {}
inp = input("Your words: ").lower()
for i in inp:
    car[i] = car.get(i, 0) + 1

for i, j in car.items():
    if(i != " "):
        print(i, j)


