def replace_not_poor(input_str):
    not_index = input_str.find('not')
    poor_index = input_str.find('poor')
    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        return input_str[:not_index] + 'good' + input_str[poor_index + 4:]
    else:
        return input_str


sample_string1 = 'The lyrics is not that poor!'
sample_string2 = 'The lyrics is poor!'
result1 = replace_not_poor(sample_string1)
result2 = replace_not_poor(sample_string2)
print(result1) 
print(result2)  
