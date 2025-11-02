def longest(arr):
    n = len(arr)
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    return max(lis)
n = [10, 22, 9, 33, 21, 50, 41, 60, 80]
result = longest(n)
print("Length of LIS:", result)