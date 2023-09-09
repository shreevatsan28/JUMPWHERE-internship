def MaxChar(s):
    c = 0
    v = ''
    for i in s:
        j = s.count(i)
        if j > c:
            c = j
            v = i
        elif j == c and ord(v) > ord(i):
            v = i
    return v

s = input("Enter a string: ")
print("The character that appears most frequently is:", MaxChar(s))
