def min_max(numbers):
    if not numbers:
        return None, None  

    smallest = largest = numbers[0]
    for num in numbers[1:]:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return smallest, largest

n = input()
numbers = list(map(int, n.split()))
min_val, max_val = min_max(numbers)
print("Minimum:", min_val)
print("Maximum:", max_val)