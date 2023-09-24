def remove_consecutive_duplicates(input_str):
    result_str = input_str[0]
    for i in range(1, len(input_str)):
        if input_str[i] != input_str[i - 1]:
            result_str += input_str[i]
    return result_str


sample_string = "aaabbbbcccddeee"
result = remove_consecutive_duplicates(sample_string)
print(result) 
