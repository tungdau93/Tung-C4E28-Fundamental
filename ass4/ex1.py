inventory = {
    "gold" : 500,
    "pouch" : ["flint", "twine", "gemstone"],
    "backpack" : ["xylophone", "dagger", "bedroll", "bread loaf"]
}
# creat new key and value
inventory["pocket"] = ["seashell", "strange berry", "lint"]
# delete 'dagger' from 'backpack'
del inventory["backpack"][1]
# add '50' to key 'gold'
inventory["gold"] += 50
for i,j in inventory.items():
    print(i, j)