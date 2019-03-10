def remove_dollar_sign(old_string):
    new_string = old_string.replace("$", "")
    return new_string

ip = input("Enter any string: ")
print(remove_dollar_sign(ip))
