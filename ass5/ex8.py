def remove_dollar_sign(old_string):
    new_string = old_string.replace("$", "")
    return new_string

string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")




