def swap_comma_and_dot(input_str):
    swapped_str = input_str.replace(',', '_').replace('.', ',').replace('_', '.')
    return swapped_str


sample_string = "32.054,23"
result = swap_comma_and_dot(sample_string)
print(result)  
