from random import randint
words1 = ["t", "s", "e", "u", "m", "o", "i", "u", "c", "l"]
words2 = ["m", "n", "c", "a", "p", "i", "h", "o"]
words3 = ["e", "h", "x", "a", "n", "g", "o"]

print("Word jumble")
a = randint(1,3)
loop = True
if(a == 1):
    while loop:
        if(len(words1) > 0):
            index = randint(0, len(words1) - 1)
            print(words1[index], end = " ")
            del words1[index]
        else:
            loop = False
    inp = input("\nYour answer: ")
    if(inp == "meticulous"):
        print("hura!")
    else:
        print(":(")
elif(a == 2):
    while loop:
        if(len(words2) > 0):
            index = randint(0, len(words2) - 1)
            print(words2[index], end = " ")
            del words2[index]
        else:
            loop = False
    inp = input("\nYour answer: ")
    if(inp == "champion"):
        print("hura!")
    else:
        print(":(")
else:
    while loop:
        if(len(words3) > 0):
            index = randint(0, len(words3) - 1)
            print(words3[index], end = " ")
            del words3[index]
        else:
            loop = False
    inp = input("\nYour answer: ")
    if(inp == "hexagon"):
        print("hura!")
    else:
        print(":(")
