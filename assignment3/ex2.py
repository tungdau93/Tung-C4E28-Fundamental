sheep = [5, 7, 300, 90, 24, 50, 75]
print("========================================================")
print("\n1. Hello, My name is Tùng and these are my sheep sizes")
print(sheep)


print("========================================================")
print("\n2. Now my biggest sheep has size", max(sheep), "let's shear it")


print("========================================================")
print("\n3. After shearing, here is my flock")
index =  sheep.index(max(sheep))
sheep[index] = 8
print(sheep)


print("========================================================")
print("\n4. One month has passed, now here is my flock")
for i in range(0,len(sheep)):
    sheep[i] += 50
print(sheep)


print("========================================================")
print("\n5. Hello, My name is Tùng and these are my sheep sizes")
sheep = [5, 7, 300, 90, 24, 50, 75]
print(sheep)
print("\nMONTH 1: ")
print("One month has passed, now here is my flock")
for i in range(0,len(sheep)):
    sheep[i] += 50
print(sheep)
print("Now my biggest sheep has size", max(sheep), "let's shear it")
print("After shearing, here is my flock")
i =  sheep.index(max(sheep))
sheep[i] = 8
print(sheep)
print("\nMONTH 2:")
print("One month has passed, now here is my flock")
for i in range(0,len(sheep)):
    sheep[i] += 50
print(sheep)
print("Now my biggest sheep has size", max(sheep), "let's shear it")
print("After shearing, here is my flock")
i =  sheep.index(max(sheep))
sheep[i] = 8
print(sheep)
print("\nMONTH 3:")
print("One month has passed, now here is my flock")
for i in range(0,len(sheep)):
    sheep[i] += 50
print(sheep)
print("Now my biggest sheep has size", max(sheep), "let's shear it")
print("After shearing, here is my flock")
i =  sheep.index(max(sheep))
sheep[i] = 8
print(sheep)


print("========================================================")
print("\n6. My flock has size in total: ", end = "")
sum = 0
for i in range(0,len(sheep)):
    sum += sheep[i]
print(sum)
print("I would get ", sum, " * 2$ = ", sum*2, "$")