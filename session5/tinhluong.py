person = [
    {"name" : "Quan", "money" : 25, "hours" : 3, "day" : 20},
    {"name" : "Duc", "money" : 80, "hours" : 5, "day" : 15}
]
print("Name\t\t$/h\t\tHour/day\tDay/month\t")
for i in range(len(person)):
    print(*person[i].values(), sep = "\t\t")

user_inp = input("Enter a name: ")
salary = 1
total = 0
for each_person in person: # thắc mắc
    # gán 1 biến found = false để hiểu là chưa tìm thấy person
    found = False
    if(user_inp == each_person["name"]):
        salary = each_person["money"] * each_person["hours"] * each_person["day"]
        found = True
        break
    else:
        found = False
if(found == True):
    print(salary)
else:
    print("Not found")

# for each_person in person:
#     total += each_person["money"] * each_person["hours"] * each_person["day"]
# print("Total salary = ", total)

