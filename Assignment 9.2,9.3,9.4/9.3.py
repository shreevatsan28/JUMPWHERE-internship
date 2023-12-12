def is_balanced_delimiters(input_string):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in input_string:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()

    return len(stack) == 0


input_str = "([{}])"
result = is_balanced_delimiters(input_str)
print(result) 
