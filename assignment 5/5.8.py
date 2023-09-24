def longest_word_length(list):
    if not list:
        return 0
    else:
        return max(len(word) for word in word_list)

word_list = ['apple', 'banana', 'cherry', 'orange', 'dragon fruit']
result = longest_word_length(word_list)
print(result)  
