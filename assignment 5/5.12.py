def convert_to_uppercase(input_str):
    uppercase_count = 0
    for char in input_str[:4]:
        if char.isupper():
            uppercase_count += 1
    
    if uppercase_count >= 2:
        return input_str.upper()
    else:
        return input_str

sample_string1 = 'AbCdEf'
sample_string2 = 'aBcDeF'
result1 = convert_to_uppercase(sample_string1)
result2 = convert_to_uppercase(sample_string2)
print(result1)  
print(result2) 