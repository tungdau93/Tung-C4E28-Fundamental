from random import randint
words = ["c", "h", "a", "m", "p", "i", "o", "n"]
print("Word jumble")

loop = True
while loop:
    if(len(words) > 0):
        index = randint(0, len(words) - 1)
        print(words[index], end = " ")
        del words[index]
    else:
        loop = False
inp = input("\nYour answer: ")
if(inp == "champion"):
    print("hura!")
else:
    print(":(")
