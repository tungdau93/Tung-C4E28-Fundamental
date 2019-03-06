# # key: value được coi là 1 cặp trong dictionary, phân cách nhau bằng dấu phẩy
# person = {
#     "name" : "Duc",
#     "age" : 22,
#     "ex" : 3,
#     "language" : "chinese"
# }

# name = person["name"]

# # READ
# for i in person.keys():
#     print(i) # in ra key
# for j in person.values():
#     print(j) # in ra values
# for i,j in person.items():
#     print(i, j) # in ra cả key + values


# # CREATE + UPDATE
# person["city"] = "Hai Phong" # create new
# person["ex"] = 10 # update
# print(person)


# # DELETE
# del person["age"] # Delete
# print(person)



tudien = {
    "name" : "tên",
    "age" : "tuổi" ,
    "book" : "sách" ,
    "computer" : "máy tính"
}
while True:
    print(*tudien.keys())
    inp = input("Your word: ")
    if inp in tudien:
        print("Your translation: ", tudien[inp])
    else:
        answer = input("Add new word? (y/n)").lower()
        if(answer == "n"):
            print("goodbye")
            break
        elif(answer == "y"):
            new_translation = input("Your word: ")
            tudien[inp] = new_translation
    