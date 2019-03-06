# chương trình đoán số của mình
print('''Now think of a number from 0 to 100, then press 'Enter'
All you have to do is to answer to my guess
'c' if my guess is 'c'orrect
's' if my guess is 's'maller' than your number
'l' if my guess is 'l'arger' than your number''')


low = 1
high = 101

while True:
    mid  = (low + high)//2
    # print("Is", mid, "your number?")
    inp = input("is {0} your number?".format(mid))
    if(inp == "c"):
        print("I knew it")
        break
    elif(inp == "l"):
        high = mid
    elif(inp == "s"):
        low = mid