def string_reversal(string):
    if len(string)%4 == 0:
        return string[::-1]
    else:
        return string
    
sample_string1 = 'abcd'
sample_string2 = 'abcde'
result1 = string_reversal(sample_string1)
result2 = string_reversal(sample_string2)
print(result1)
print(result2)