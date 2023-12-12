def kth_largest(arr, n, k):
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    
    return arr[n - k]

n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter element {}:".format(i + 1))))

k = int(input("Enter the value of k: "))
result = kth_largest(arr, n, k)

print("kth largest element:", result)
