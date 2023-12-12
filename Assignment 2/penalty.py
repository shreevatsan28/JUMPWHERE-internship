def penaltyScore(S):
    c = 0
    for i in range(len(S) - 1):
        if S[i:i+2] == '21':
            c += 1
    return c

S = input("Enter the penalty shootout sequence: ")
print("Number of times the second team scores immediately after the first team:", penaltyScore(S))
