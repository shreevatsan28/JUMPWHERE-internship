def get_first_and_last_chars(input_str):
    if len(input_str) < 2:
        return ""
    else:
        return input_str[:2] + input_str[-2:]

sample_str= 'thisisniceone'
result = get_first_and_last_chars(sample_str)
print(result) 
