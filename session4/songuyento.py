# số nguyên tố
n = int(input("n = "))
is_prime = True
i = 2
if(n < 2):
    print("n ko là số nguyên tố")
else:
    while (i < n):
        if(n%i == 0):
            is_prime = False
            break
        i += 1
    if(is_prime == True):
        print("n là số nguyên tố")
    else:
        print("n ko là số nguyên tố")
        

