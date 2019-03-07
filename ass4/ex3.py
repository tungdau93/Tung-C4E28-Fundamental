ex4 = {
    1 : 35,
    2 : 36,
    3 : 40,
    4 : 44
}
while True:
    print('''Answer the following algebra question
If x = 8, then what is the value of 4(x + 3) ?''')
    for i,j in ex4.items():
        print(i,j, sep = ". ")
    choice = int(input("Your choice: "))
    if(choice == 4):
        print("Bingo!")
        break
    elif(choice == 1 or choice == 2 or choice == 3):
        print(":(")
    else:
        print("Only allowed 1->4. Again!")
