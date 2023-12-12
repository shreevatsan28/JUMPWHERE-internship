def remove_nth_character(str, n):
    if 0 <= n < len(str):
        return str[:n] + str[n+1:]
    else:
        return str


sample_string = 'abcdefg'
n = 2
result = remove_nth_character(sample_string, n)
print(result)
