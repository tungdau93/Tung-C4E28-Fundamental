from random import randint
import random
from random import choice
words = "champion"
random_char = []
list_word = list(words)
while(len(list_word) > 0):
    chars = choice(list_word)
    random_char.append(chars)
    list_word.remove(chars)
print(*random_char)


# c = list(words)
# print("Word jumble")
# random.shuffle(words)
# print(*words)


# loop = True
# while loop:
#     if(len(words) > 0):
#         index = randint(0, len(words) - 1)
#         print(words[index], end = " ")
#         del words[index]
#     else:
#         loop = False

inp = input("Your answer: ")
if(inp == "champion"):
    print("hura!")
else:
    print(":(")
