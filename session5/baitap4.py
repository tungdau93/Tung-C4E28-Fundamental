from random import randint, choice
# from calculate import eval
import calculate
x = randint(0,10)
y = randint(0,10)
op = choice(["+", "-", "*", "/"])

errors = randint(-1,1)
print(errors)
result = calculate.eval(x, y, op)
# result = eval(x, y, op)
random_result = result + errors

print("{0} {1} {2} = {3}".format(x, op, y, random_result))

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






