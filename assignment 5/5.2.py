def count_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
    return char_count

count = count_characters(input("Enter the string:"))
print(count)
