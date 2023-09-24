def unique_words_sorted(str):
    words = str.split(', ')
    unique_words = sorted(set(words))
    return ', '.join(unique_words)


sample_words = 'red, white, black, red, green, black'
result = unique_words_sorted(sample_words)
print(result)
