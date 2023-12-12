def find_smallest_largest_word(input_str):
    words = input_str.split()
    if not words:
        return None, None
    smallest_word = min(words, key=len)
    largest_word = max(words, key=len)
    return smallest_word, largest_word

sample_string = "This is a simple example"
smallest, largest = find_smallest_largest_word(sample_string)
print("Smallest word:", smallest)  
print("Largest word:", largest)    
