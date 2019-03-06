from random import randint
import random
from random import choice

words1 = ["t", "s", "e", "u", "m", "o", "i", "u", "c", "l"]
words2 = ["m", "n", "c", "a", "p", "i", "h", "o"]
words3 = ["e", "h", "x", "a", "n", "g", "o"]

print("Word jumble")
a = randint(1,3)
loop = True
if(a == 1):
    random.shuffle(words1)
    print(*words1)
    inp = input("\nYour answer: ")
    if(inp == "meticulous"):
        print("hura!")
    else:
        print(":(")
elif(a == 2):
    random.shuffle(words2)
    print(*words2)
    inp = input("\nYour answer: ")
    if(inp == "champion"):
        print("hura!")
    else:
        print(":(")
else:
    random.shuffle(words3)
    print(*words3)
    inp = input("\nYour answer: ")
    if(inp == "hexagon"):
        print("hura!")
    else:
        print(":(")

