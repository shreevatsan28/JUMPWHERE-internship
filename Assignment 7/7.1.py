dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
sorted_dict1_asc = {k: v for k, v in sorted(dict1.items(), key=lambda item: item[1])}
print("Sorted dictionary in ascending order: ", sorted_dict1_asc)
sorted_dict1_desc = {k: v for k, v in sorted(dict1.items(), key=lambda item: item[1], reverse=True)}
print("Sorted dictionary in descending order: ", sorted_dict1_desc)