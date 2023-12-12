def char_index(input_str, char):
    if char in input_str:
        return input_str.index(char)
    else:
        return -1


sample_string = 'abcdefg'
char = 'c'
char_result = char_index(sample_string,char)
print(char_result)
