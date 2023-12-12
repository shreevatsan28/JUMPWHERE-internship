def count_repeated_characters(input_str):
    char_count = {}
    for char in input_str:
        if char.isalpha():
            char = char.lower()
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    repeated_chars = {char: count for char, count in char_count.items() if count > 1}
    return repeated_chars

sample_string = 'thequickbrownfoxjumpsoverthelazydog'
result = count_repeated_characters(sample_string)
for char, count in result.items():
    print(char, count)
