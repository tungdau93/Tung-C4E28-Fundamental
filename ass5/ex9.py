def get_even_list(old_list):
    new_list = []

    for i in range(len(old_list)):
        if(old_list[i] % 2 == 0):
            new_list.append(old_list[i])
    
    return new_list

number_list = []
length_list = int(input("Enter length of a number list: "))

for i in range(length_list):
    ip = int(input("a[{0}] = ".format(i)))
    number_list.append(ip)

print("Your current list: ", number_list)

while True:
    question = input("Continute add to list. Y/N? ").upper()

    if(question == "Y"):
        length_list = int(input("Enter length of a number add to list: "))

        for i in range(length_list):
            ip = int(input("a[{0}] = ".format(i)))
            number_list.append(ip)

    elif(question == "N"):
        break
    
    print("Your current list: ", number_list)

print("Your even number list: ", get_even_list(number_list))
        
