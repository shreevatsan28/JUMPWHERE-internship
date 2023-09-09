def kth_perm(n, k):
    def factorial(x):
        result = 1
        for i in range(2, x + 1):
            result *= i
        return result

    permutation = []
    numbers = list(range(1, n + 1))

    k -= 1  

    for _ in range(n):
        fact = factorial(n - 1)
        index = k // fact
        k %= fact
        permutation.append(numbers.pop(index))
        n -= 1

    return ''.join(map(str, permutation))

print(kth_perm(3, 3))
