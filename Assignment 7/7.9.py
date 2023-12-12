my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
product = 1
for key in my_dict:
    product *= my_dict[key]
print("The product of all items in the dictionary is:", product)