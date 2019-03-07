prices = {
    "banana" : 4,
    "apple" : 2,
    "orange" : 1.5,
    "pear" : 3
}
stock = {
    "banana" : 6,
    "apple" : 0,
    "orange" : 32,
    "pear" : 15
}
total = 0
print("=======================")
for i in prices.keys():
    print(i)
    print("Prices:", prices[i])
    print("Stock:", stock[i])
    print()

print("=======================")
for i in prices.keys():
    multi = prices[i] * stock[i]
    print(i, multi)
    total += multi
print("Total =", total)
