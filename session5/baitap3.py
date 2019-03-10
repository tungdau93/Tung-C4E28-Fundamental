from random import randint

x = randint(0,10)
y = randint(0,10)

errors = randint(-1,1)
result = x + y
random_result = result + errors

print("{} + {} = {}".format(x, y, random_result))

answer = input("Y/N? ").upper()
if(answer == "Y"):
    if(errors == 0):
        print("Correct!")
    else:
        print("Wrong!")
if(answer == "N"):
    if(errors == 0):
        print("Wrong!")
    else:
        print("Correct!")






