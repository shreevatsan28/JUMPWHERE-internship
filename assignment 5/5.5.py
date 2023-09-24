def swap_2_string_chars(str1,str2):
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str2[:2] + str1[2:]
    out_str = new_str1 + ' ' +  new_str2
    return out_str

sample_str1 = 'abc'
sample_str2 = 'xyz'
result = swap_2_string_chars(sample_str1,sample_str2)
print(result)