ex41 = {
    1 : 35,
    2 : 36,
    3 : 40,
    4 : 44
}
ex42 = {
    1 : "About 55",
    2 : "About 65",
    3 : "About 75",
    4 : "About 85"
}
count = 0
print('''Answer the following algebra question
If x = 8, then what is the value of 4(x + 3) ?''')
for i,j in ex41.items():
    print(i,j, sep = ". ")
choice1 = int(input("Your choice: "))
if(choice1 == 4):
    print("Bingo!")
    count += 1
else:
    print(":(")

print('''Estimate this answer (exact calculation not needed:
Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?''')
for i,j in ex42.items():
    print(i,j, sep = ". ")
choice2 = int(input("Your choice: "))
if(choice2 == 2):
    print("Bingo!")
    count += 1
else:
    print(":(")
print("You correctly answer {0} out of 2 questions".format(count))
