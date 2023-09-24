def first_char_occurence(string):
    if len(string)<2:
        return string
    else:
        first_char = string[0]
        new_str = string[0] + string[1:].replace(first_char,'$')
        return new_str
    
sample_str = 'restart'
result = first_char_occurence(sample_str)
print(result)