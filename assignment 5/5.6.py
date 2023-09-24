def add_suffix(input_str):
    if len(input_str) < 3:
        return input_str
    elif input_str.endswith('ing'):
        return input_str + 'ly'
    else:
        return input_str + 'ing'


sample_string1 = 'abc'
sample_string2 = 'string'
result1 = add_suffix(sample_string1)
result2 = add_suffix(sample_string2)
print(result1)  
print(result2)  
